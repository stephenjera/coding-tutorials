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

        this.draw();
    }
}

// Animating the circle
var circleArray = [];


for (var i = 0; i < 100; i++) {
    var radius = 30;
    var x = Math.random() * (innerWidth - radius * 2) + radius; // Random x location
    var y = Math.random() * (innerHeight - radius * 2) + radius; // Random y location
    var dx = (Math.random() - 0.5); // Change in x velocity
    var dy = (Math.random() - 0.5) ; // Change in y velocity
    circleArray.push(new Circle(x, y, dx, dy, radius));  
}

console.log(circleArray);


// Animation function
function animate() {
    requestAnimationFrame(animate); // Creates the animation loop
    c.clearRect(0, 0, innerWidth, innerHeight); // Clears canvas
    // Draws circles 
    for (var i = 0; i < circleArray.length; i++) {
        circleArray[i].update();
    }
    
}

animate(); 
