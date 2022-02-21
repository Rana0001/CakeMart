let sum = 1
function add() {
    sum = sum + 1
    document.getElementById("quantity").value = sum
}

function sub() {
    if (sum > 1) {
        sum = sum - 1
        document.getElementById("quantity").value = sum
    }
}