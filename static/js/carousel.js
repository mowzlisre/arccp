

function reviewFunc() {
    var x = document.getElementsByClassName("carousel-item active")
    var number = x[0].firstElementChild.innerText[8, 9]
    document.getElementById("data-slide-" + number).classList.add("bg-warning", "text-white")
}
function submitFun() {
    var y = document.getElementsByClassName("bg-warning")
    if (y.length == 0) {
        var cnfrm = confirm(
            "Are you sure you want to complete the test?")
        if (cnfrm == true) {
            document.getElementById("form-main").submit()
        }
    } else {
        var cnfrm = confirm(
            "You have questions to review! Are you sureyou want to complete the test?")
        if (cnfrm == true) {
            document.getElementById("form-main").submit()
        }
    }
}
function selectFun(){
    var x = document.getElementsByClassName("carousel-item active")
    var number = x[0].firstElementChild.innerText[8, 9]
    document.getElementById("data-slide-" + number).classList.add("bg-primary", "text-white") 
}