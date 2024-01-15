from Player import Player
import tkinter as tk 
import os
import time
from Deck import Deck

def initialize_game():
    startingFrame.forget()
    dealerFrame.pack(pady=20)
    roundMessageFrame.pack(pady=20)
    playerFrame.pack(side="bottom", pady=20)

    deck.shuffle()
    start_round()

def start_round():
    dealer.add_cards(deck.deal())
    dealer.add_cards(deck.deal())

    player.add_cards(deck.deal())
    player.add_cards(deck.deal())

    message['text'] = "..."

    dealerCard['text'] = str(dealer.peak_deck()[0])
    playerCard['text'] = str(player.peak_deck())

def call_card():
    result = player.add_cards(deck.deal())
    playerCard['text'] = str(player.peak_deck())

    if (result == "exceed"):
        callButton['state'] = "disabled"
        standButton['state'] = "disabled"
        message['text'] = "your card exceeds 21... wait for dealer"
        mainWindow.update_idletasks()
        time.sleep(1)
        dealer_turn()


def stand_card():
    callButton['state'] = "disabled"
    standButton['state'] = "disabled"
    message['text'] = "You stand your card"
    mainWindow.update_idletasks()
    time.sleep(1)
    dealer_turn()

def dealer_turn():
    con = True

    message['text'] = "dealer's turn"

    while con:
        dealerCard['text'] = dealer.peak_deck()
        mainWindow.update_idletasks()
        time.sleep(0.5)
        if (dealer.peak_value() >= 17) or (dealer.peak_value() == -1):
            con = False
        elif (dealer.peak_value() <= 16):
            dealer.add_cards(deck.deal())

    time.sleep(1)
    calculate_win()

def calculate_win():
    if (player.peak_value() > dealer.peak_value()) or (dealer.peak_value() == -1):
        message['text'] = "Player won"
    else:
        message['text'] = "Dealer won"

    continueButton.pack()

def next_round():
    continueButton.pack_forget()
    dealer.reset()
    player.reset()
    callButton['state'] = "normal"
    standButton['state'] = "normal"
    message['text'] = "restarting..."
    mainWindow.update_idletasks()
    time.sleep(2)
    start_round()

def restart():
    print("restart")        

mainWindow = tk.Tk()
mainWindow.geometry("600x400")
mainWindow.title("Black Jack")

startingFrame = tk.Frame(mainWindow)
startingFrame.pack()

dealerFrame = tk.Frame(mainWindow)
roundMessageFrame = tk.Frame(mainWindow)
playerFrame = tk.Frame(mainWindow)

welcomeLabel = tk.Label(startingFrame, text = "Welcome to Black Jack", font=25)
initializeButton = tk.Button(startingFrame, text="start", command=initialize_game)
welcomeLabel.pack()
initializeButton.pack()

dealerLabel = tk.Label(dealerFrame, text="Dealer")
dealerLabel.pack()
dealerCard = tk.Label(dealerFrame, text="empty", font=15)
dealerCard.pack(pady=15)

message = tk.Label(roundMessageFrame, text="...", font=15)
message.pack(pady=10)

playerLabel = tk.Label(playerFrame, text="Player")
playerLabel.pack()
playerCard = tk.Label(playerFrame, text="empty", font=15)
playerCard.pack(pady=15)

callButton = tk.Button(playerFrame, text="Call", command=call_card, font=13)
callButton.pack(side="left", padx=40, pady=5)
standButton = tk.Button(playerFrame, text="Hold", command=stand_card, font=13)
standButton.pack(side="right", padx=40, pady=5)
continueButton = tk.Button(playerFrame, text="continue", command=next_round, font=13)
restartButton = tk.Button(playerFrame, text="restart", command=restart, font=13)

deck = Deck()
dealer = Player(100)
player = Player(100)
dealer.set_dealer()

mainWindow.mainloop()


