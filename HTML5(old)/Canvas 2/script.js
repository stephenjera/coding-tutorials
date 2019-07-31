// JavaScript source code

// Creating multiple circles
function Circle(x,y) {
    this.x = x;
    this.y = y;

    this.draw = function () {
        console.log("draw");
    }
}

var circle = new Circle(200, 200);

var canvas = document.querySelector("canvas");

// Resisizing window
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Replaceing ctx wit c
var c = canvas.getContext("2d");

// Animating the circle
var x = Math.random() * innerWidth;
var y = Math.random() * innerHeight;
var dx = (Math.random() - 0.5) * 10; // Change in x velocity
var dy = (Math.random() - 0.5) * 10; // Change in y velocity
var radius = 30;


function animate() {
    requestAnimationFrame(animate); // Creates the animation loop
    console.log("animate");

    //Circle function
    c.clearRect(0, 0, innerWidth, innerHeight);
    c.beginPath(); // Creates new start point
    c.arc(x, y, radius, 0, Math.PI * 2, false); // Only give outline
    c.strokeStyle = "blue";
    c.stroke();// Draw circle

    // Prevents Circle from exiting the window
    if (x + radius > innerWidth || x - radius < 0) {
        dx = -dx;
    }
    if (y + radius > innerHeight || y - radius < 0) {
        dy = -dy;
    }

    
    // Velocity control variable
    x += dx;
    y += dy;
}

animate(); // executes the code

console.log(canvas);