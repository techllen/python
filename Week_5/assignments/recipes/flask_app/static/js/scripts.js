console.log("CONNECTED TO JS")

//this method makes the error div appear and disappear 
function error_visibility(){
    const errorsDivs = document.querySelector('div')

    // checking what type of errors are present
    // when register errors are present
    if (document.querySelector('li').classList.contains("register-error") == true ){
        document.getElementById('registererrors').style.display = 'block'
    // when login errors are present
    } else if (document.querySelector('li').classList.contains("login-error") == true){
        document.getElementById('loginerrors').style.display = 'block'
    }
}

// Running error visibility function
error_visibility()




