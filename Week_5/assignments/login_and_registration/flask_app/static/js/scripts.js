// console.log("CONNECTED TO JS")
// this method change password visibility
function showPassword() {
    var pwd = document.getElementById("password");
    var cpwd = document.getElementById("confirmed_password");
    if (pwd.type === "password") {
        pwd.type = "text";
    } else {
        pwd.type = "password";
    }

    if (cpwd.type === "password" ) {
        cpwd.type = "text";
    } else {
        cpwd.type = "password";
    }
  }