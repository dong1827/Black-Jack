var loginForm = document.getElementById("login");

function showRegister() {
    
    /*<form id="login" action = "/login" method = "post"> 
    <label for = "password" title = "Enter your password">Password: </label><br>
    <input type = "password" id = "password" name = "password" form = "login"><br> 
    */ 
    const registerForm = loginForm.cloneNode(true);
    registerForm.setAttribute("id", "register");
    registerForm.setAttribute("action", "/register");
    registerForm.setAttribute("method", "post");

    loginForm.replaceWith(registerForm);

    const passLabel = document.createElement("label");
    const passInput = document.createElement("input");
    const linebreak = document.createElement("br");
    const logBut = document.getElementById("login-button");

    passLabel.setAttribute("for", "retype");
    passLabel.setAttribute("title", "Please type your password again");
    passLabel.textContent = "Retype password:";
    
    passInput.setAttribute("type", "password");
    passInput.setAttribute("id", "retype");
    passInput.setAttribute("name", "retype");
    passInput.setAttribute("form", "register");
    passInput.setAttribute("class", "space-at-bottom");

    logBut.setAttribute("onclick", "showLogin()");

    document.getElementById("register-button").setAttribute("onclick", "submitRegister()");
    document.getElementById("username").setAttribute("form", "register");
    document.getElementById("password").setAttribute("form", "register");

    registerForm.insertBefore(passLabel, logBut);
    registerForm.insertBefore(linebreak, logBut);
    registerForm.insertBefore(passInput, logBut);
    registerForm.insertBefore(linebreak, logBut);
    
    document.getElementById("login-div").setAttribute("class", "register-box");
}

function showLogin() {
    document.getElementById("register").replaceWith(loginForm);
    document.getElementById("register-button").setAttribute("onclick", "showRegister()");
    document.getElementById("login-div").setAttribute("class", "login-box");
}

function submitLogin() {
    document.getElementById("login").submit();
}

function submitRegister() {
    const pass = document.getElementById("password");
    const retype = document.getElementById("retype");
    
    if (pass.value != retype.value) {
        // do some error display
    }
    else {
        document.getElementById("register").submit();
    }
    
}
