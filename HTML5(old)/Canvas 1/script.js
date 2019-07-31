// JavaScript source code

var canvas = document.querySelector("canvas");

// Resisizing window
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Replaceing ctx wit c
var c = canvas.getContext("2d");

// Drawing a rectangle
c.fillStyle = "rgba(255, 0, 0, 0.51)"; // Changes colour of rect after it
c.fillRect(100, 100, 100, 100);
c.fillStyle = "rgba(255, 200, 0, 0.51)"; // Changes colour of rect after it
c.fillRect(400, 100, 100, 100);
c.fillStyle = "rgba(255, 0, 200, 0.51)"; // Changes colour of rect after it
c.fillRect(100, 500, 100, 100);

// Drawing lines
c.beginPath(); 
c.moveTo(50, 300); // Start point of line
c.lineTo(300, 100); // End point of line
c.lineTo(400, 200);
c.strokeStyle = "#666"; // Changes stroke colour
c.stroke(); // Draws line

// Drawing arc/circle
c.beginPath(); // Creates new start point
c.arc(300, 300, 30, 0, Math.PI * 2, false); // Only give outline
c.strokeStyle = "blue";
c.stroke();// Draw circle


// Creating multiple circles with for loop
for (var i = 0; i < 3; i++) {
    var x = Math.random() * window.innerWidth;
    var y = Math.random() * window.innerHeight;
    c.beginPath(); // Creates new start point
    c.arc(x, y, 30, 0, Math.PI * 2, false); // Only give outline
    c.strokeStyle = "blue";
    c.stroke();// Draw circle
}









console.log(canvas);
