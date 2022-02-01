var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("navbar").style.top = "0";
    } else {
        document.getElementById("navbar").style.top = "-120px";
    }
    prevScrollpos = currentScrollPos;
}



// Slider JS



const slides = document.querySelector(".slider-content").children;
const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
const indicator = document.querySelector(".indicator");
let index = 0;


prev.addEventListener("click", function () {
    prevSlide();
    updateCircleIndicator();
    resetTimer();
})

next.addEventListener("click", function () {
    nextSlide();
    updateCircleIndicator();
    resetTimer();

})

// create circle indicators
function circleIndicator() {
    for (let i = 0; i < slides.length; i++) {
        const div = document.createElement("div");
        div.innerHTML = i + 1;
        div.setAttribute("onclick", "indicateSlide(this)")
        div.id = i;
        if (i == 0) {
            div.className = "active-slide";
        }
        indicator.appendChild(div);
    }
}
circleIndicator();

function indicateSlide(element) {
    index = element.id;
    changeSlide();
    updateCircleIndicator();
    resetTimer();
}

function updateCircleIndicator() {
    for (let i = 0; i < indicator.children.length; i++) {
        indicator.children[i].classList.remove("active-slide");
    }
    indicator.children[index].classList.add("active-slide");
}

function prevSlide() {
    if (index == 0) {
        index = slides.length - 1;
    }
    else {
        index--;
    }
    changeSlide();
}

function nextSlide() {
    if (index == slides.length - 1) {
        index = 0;
    }
    else {
        index++;
    }
    changeSlide();
}

function changeSlide() {
    for (let i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active-slide");
    }

    slides[index].classList.add("active-slide");
}

function resetTimer() {
    // when click to indicator or controls button 
    // stop timer 
    clearInterval(timer);
    // then started again timer
    timer = setInterval(autoPlay, 4000);
}


function autoPlay() {
    nextSlide();
    updateCircleIndicator();
}

let timer = setInterval(autoPlay, 4000);






