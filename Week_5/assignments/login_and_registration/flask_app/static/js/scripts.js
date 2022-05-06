// console.log("CONNECTED TO JS")
//this method makes the error div appear and disappear 
var register_error_div_content = document.getElementById('registererrors').innerHTML.length
console.log(register_error_div_content)

if (register_error_div_content>72){
    document.getElementById('registererrors').style.display = 'block'
}

var login_error_div_content = document.getElementById('loginerrors').innerHTML.length
console.log(login_error_div_content)

if (login_error_div_content> 84){
    document.getElementById('loginerrors').style.display = 'block'
    document.getElementById('registererrors').style.display = 'none'
}

console.log(document.getElementById('registererrors').innerHTML)
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

