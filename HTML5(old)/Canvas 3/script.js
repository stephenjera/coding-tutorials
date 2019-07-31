// JavaScript source code

var canvas = document.querySelector("canvas");

// Resisizing window
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Replaceing ctx wit c
var c = canvas.getContext("2d");

// Creating multiple circles
function Circle(x, y, dx, dy, radius) {
    this.x = x;
    this.y = y;
    this.dx = dx;
    this.dy = dy;
    this.radius = radius;

    this.draw = function () {
        c.beginPath(); // Creates new start point
        c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false); // Only give outline
        c.strokeStyle = "blue";
        c.stroke();// Draw circle
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

        this.draw();
    }
}

var circle = new Circle(200, 200, 3, 3, 30);


// Animating the circle
var x = Math.random() * innerWidth; // Random x location
var y = Math.random() * innerHeight; // Random y location
var dx = (Math.random() - 0.5) * 10; // Change in x velocity
var dy = (Math.random() - 0.5) * 10; // Change in y velocity
var radius = 30;

// Animation function
function animate() {
    requestAnimationFrame(animate); // Creates the animation loop
    c.clearRect(0, 0, innerWidth, innerHeight);

    circle.update();

    //Circle function
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

    x += dx; // Velocity control variables
    y += dy;
}

animate(); 
