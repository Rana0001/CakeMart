
var state = false
function showPassword() {
    if (state) {
        document.getElementById("password-field").setAttribute("type", "password");
        document.getElementById("eye").setAttribute("src", "/static/images/eye/eyeclosed.svg");

        state = false;

    } else {
        document.getElementById("password-field").setAttribute("type", "text");
        document.getElementById("eye").setAttribute("src", "/static/images/eye/eyeopen.svg");
        state = true;
    }

}
