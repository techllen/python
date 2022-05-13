console.log("CONNECTED TO JS")

//this method makes the error div appear and disappear 
function error_visibility(){
    const errorsDivs = document.querySelector('div')
    console.log(document.querySelector('li').classList.contains("register-error"))

    // checking what type of errors are present
    // when register errors are present
    if (document.querySelector('li').classList.contains("register-error") == true){
        document.getElementById('registererrors').style.display = 'block'
        // console.log(errorsDivs.classList.contains('register-error'))
        // console.log("me"+document.querySelector('li'))
    // when login errors are present
    } else if (document.querySelector('li').classList.contains("login-error") == true){
        document.getElementById('loginerrors').style.display = 'block'
        // console.log(errorsDivs.classList.contains('login-error'))
    } else if (document.querySelector('li').classList.contains("message-error") == true){
        document.getElementById('messageerror').style.display = 'block'
        // console.log(errorsDivs.classList.contains('login-error'))
    }
}

// Running error visibility function
error_visibility()

// this method change password visibility
function showPassword() {
    var pwd = document.getElementById("password");
    var cpwd = document.getElementById("confirmed_password");
    if (cpwd.type === "password" ) {
        cpwd.type = "text";
        pwd.type = "text";
    } else {
        cpwd.type = "password";
        pwd.type = "text";
    }
  }

