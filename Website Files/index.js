function validate() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username == "h" && password == "w") {
        alert("login sucessful");
        var url = "signup.html"
        window.open(url, '-self');
        return false;
    } else {
        alert("Invalid Username and password");
    }


}