// JavaScript source code

var canvas = document.querySelector("canvas");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Replaceing ctx wit c
var c = canvas.getContext("2d");

// Adding interactivity 
var mouse = {
    x: undefined, y: undefined // To be set within mouse move event listener
}

var maxRadius = 40;
//var minRadius = 5;
var colorArray = [
    "#0872A7",
    "#EFF7F7",
    "#F4A23C",
    "#08AAA7",
    "#2E2E2E"
];

console.log(colorArray.length);

window.addEventListener("mousemove", function (event) {
    // Gets x and y locations of mouse
    mouse.x = event.x;
    mouse.y = event.y;
    // console.log(mouse);
});

// Resisizing window
window.addEventListener("resize", function () {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    init();
});


// Creating multiple circles
function Circle(x, y, dx, dy, radius) {
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.radius = radius;
    this.minRadius = radius;
    this.color = colorArray[Math.floor(Math.random() * colorArray.length)];

    this.draw = function () {
        c.beginPath(); // Creates new start point
        c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false); // Only gives outline
        //c.strokeStyle = "blue";
       // c.stroke();// Draw circle
        c.fillStyle = this.color;
        c.fill();
    }

    this.update = function () {

        if (this.x + this.radius > innerWidth || this.x - this.radius < 0) {
            this.dx = -this.dx;
        }
        if (this.y + this.radius > innerHeight || this.y - this.radius < 0) {
            this.dy = -this.dy;
        }

        this.x += this.dx; // Velocity control variables
        this.y += this.dy;

        // Interactivity
        // Sets the limit of interaction zone
        if (mouse.x - this.x < 50 && mouse.x - this.x > -50
            && mouse.y - this.y < 50 && mouse.y - this.y > -50) {
            //Prevents Circles from growing too big
            if (this.radius < maxRadius) {
                this.radius += 1; // Changes radius of circles by 1
            }
        }
        // Prevents circle radius going below zero
        else if (this.radius > this.minRadius) {
            this.radius -= 1;       
        }

        this.draw();
    }

}


var circleArray = [];

// Dynamically fill space when window is resized
function init() {
    circleArray = []; // Resetting the array
    // Animating the circle
    for (var i = 0; i < 800; i++) {
        var radius = Math.random() * 3 + 1;
        var x = Math.random() * (innerWidth - radius * 2) + radius; // Random x location
        var y = Math.random() * (innerHeight - radius * 2) + radius; // Random y location
        var dx = (Math.random() - 0.5); // Change in x velocity
        var dy = (Math.random() - 0.5); // Change in y velocity
        circleArray.push(new Circle(x, y, dx, dy, radius));
    }
}
// Animation function
function animate() {
    requestAnimationFrame(animate); // Creates the animation loop
    c.clearRect(0, 0, innerWidth, innerHeight); // Clears canvas
    // Draws circles 
    for (var i = 0; i < circleArray.length; i++) {
        circleArray[i].update();
    }

}

init();
animate(); 


