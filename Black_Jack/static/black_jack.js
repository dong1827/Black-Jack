function initialize_game() {
    fetch("/start", {
        method: 'GET',
        headers: {
            'Content-Type': 'text/html',
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('HTTP Error! Status: ${response.status}');
        }

        return response.text();
    })
    .then(htmlContent => {
        document.getElementById('display').innerHTML = htmlContent;
    })

}

function deal(){
    fetch("/deal", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('HTTP Error! Status: ${response.status}');
        }

        return response.json();
    })
    .then(async data => {
        document.getElementById('round_message').innerText = data.result
        document.getElementById('player').insertAdjacentHTML("beforeend", data.html);
        if (data.result == 'exceed') {
            await wait(3000);
            document.getElementById('round_message').innerText = "Dealer's turn";
        }
        
    })
}

async function hold(){
    document.getElementById('round_message').innerHTML = "Hold"
    await wait(3000);
    dealer()
}

function dealer(){
    deal_button = document.getElementById('deal_button')
    hold_button = document.getElementById('hold_button')
    deal_button.textContent = 'Quit'
    hold_button.text = 'Continue'
    deal_button.onclick = quit()
    hold_button.onclick = restart()
    fetch('/dealer', {
        method: 'GET',
        headers: {
            'Content-Type': 'text/html',
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('HTTP Error! Status: ${response.status}');
        }

        return response.json();
    })
    .then(async data => {
        document.getElementById('round_message').innerText = data.result
        document.getElementById('dealer').innerHTML = data.html;
    })
}

function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

function quit() {

}

function restart() {
    
}