from flask import Flask, render_template, make_response, request, session, url_for, jsonify
from Player import Player
from Deck import Deck
import pyodbc
import json

app = Flask(__name__)
app.secret_key = "RD_Black_Jack_App"

def get_connection():
    # Establishing a database connection
    server = "DESKTOP-KMAD9BP"
    database = "Black_Jack"
    user = "BlackJack"
    password = "Sqltest123!"
    driver = "{ODBC Driver 17 for SQL Server}"

    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={password}'

    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.Error as e:
        # Change this to something else later
        print(f"An error has occured while connecting to database: {e}")


# Default page
@app.route('/')
def index():
    if 'User' in session:
        return render_template('GameInterface.html', user = session['User'])
    else: 
        return render_template('index.html')

@app.route('/login', methods = ['post']) 
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Change
    sql = 'SELECT Password FROM Users WHERE Username = ?'
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(sql, username)
    result = cursor.fetchall()

    if result: 
        if result[0][0] == password:
            # Replace this tester with something else
            session['User'] = username
            response = make_response()
            # response.set_cookie('User', username)
            response.headers["Location"] = '/'
            response.status_code = 302
            
            return response
    
    else: 
        return render_template('dummy.html', user = 'wrong', password = password)

@app.route('/register', methods = ['post'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    
    sql = 'INSERT INTO Users(Username, Password) VALUES (?, ?)'
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(sql, username, password)
    conn.commit()

    return render_template('index.html', user = username, password = password, message = "Successfully Registered")

@app.route('/start', methods = ['get'])
def initialize_game():
    # if 'Deck' in session:....

    deck = Deck()
    deck.shuffle()
    player = Player()
    dealer = Player()

    dealer.add_cards(deck.deal())
    dealer.add_cards(deck.deal())

    player.add_cards(deck.deal())
    player.add_cards(deck.deal())

    update_session_var(deck.get_deck()[4:], dealer, player)

    player_imgs = []
    player_des = []

    for c in player.peak_deck():
        file = "imgs/" + str(c[0]) + str(c[1]) + ".png"
        img = url_for('static', filename = file)
        des = str(c[0]) + " of " + str(c[1])
        player_imgs.append(img)
        player_des.append(des)

    dealer_imgs = []
    dealer_des = []

    file = "imgs/" + str(dealer.peak_deck()[0][0]) + str(dealer.peak_deck()[0][1]) + ".png"
    img = url_for('static', filename = file)
    des = str(dealer.peak_deck()[0][0]) + " of " + str(dealer.peak_deck()[0][1])
    dealer_imgs.append(img)
    dealer_des.append(des)

    unknow_card = url_for('static', filename = "imgs/unknown.png")
    des = "hidden card"
    dealer_imgs.append(unknow_card)
    dealer_des.append(des)

    html = render_template("PlayScreen.html", dealer_img=zip(dealer_imgs, dealer_des), player_img=zip(player_imgs, player_des))

    response = make_response(html)
    response.headers['Content-Type'] = 'text/html'

    return response

@app.route('/deal', methods = ['get'])
def deal():
    deck = session['Deck']
    player = Player(session['Player'])

    result = player.add_cards(deck[0])

    file = "imgs/" + str(deck[0][0]) + str(deck[0][1]) + ".png"
    img = url_for('static', filename = file)
    des = str(deck[0][0]) + " of " + str(deck[0][1])

    update_session_var(deck=deck[1:], player=player)

    html = render_template("imgs.html", img_url = img, des = des)
    
    data = {"result": result, "html": html}
    response = make_response(jsonify(data))
    response.headers['Content-Type'] = 'application/json'

    return response

@app.route('/dealer', methods = ['get'])
def dealer_turn():
    deck = session['Deck']
    dealer = Player(session['Dealer'])
    imgs = [dealer.peak_deck()[0], dealer.peak_deck()[1]]

    while True:
        if (dealer.peak_value() >= 17) or (dealer.peak_value() <= -1):
            break
        else:
            dealer.add_cards(deck[0])
            imgs.append(deck[0])
            deck = deck[1:]

    html = ""
    
    for i in range(0, len(imgs)):
        file = "imgs/" + str(imgs[i][0]) + str(deck[i][1]) + ".png"
        img = url_for('static', filename = file)
        des = str(deck[i][0]) + " of " + str(deck[i][1])
        html = html + render_template("imgs.html", img_url = img, des = des)

    update_session_var(deck, dealer)
    result = calculate_result()

    data = {'result': result, 'html': html} 
    response = make_response(jsonify(data))
    response.headers['Content-Type'] = 'application/json'

    return response
    

def update_session_var(deck, dealer: Player = None, player: Player = None):
    session['Deck'] = deck
    
    if dealer is not None:
        session['Dealer'] = (dealer.peak_deck(), dealer.peak_value())
    
    if player is not None:
        session['Player'] = (player.peak_deck(), player.peak_value())

def calculate_result():
    result = ""
    dealer_value = session['Dealer'][1]
    player_value = session['Player'][1]

    if (player_value > dealer_value) or (dealer_value == -1):
        result = "player wins"
    else:
        result = "dealer wins"

    return result


if __name__ == '__main__':
  app.run(debug=True)