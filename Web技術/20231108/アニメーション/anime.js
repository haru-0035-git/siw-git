var canvas = document.getElementById("cv");
var ctx = canvas.getContext("2d");
var x = canvas.width-780;
var y =canvas.height-780;
var dx = 2;
var dy = 0;
function drawBall() {
 ctx.beginPath();
 ctx.arc(x, y, 10, 0, Math.PI*2);
 ctx.fillStyle = "#0095DD";
 ctx.fill();
 ctx.closePath();
}
function draw() {
 ctx.clearRect(0, 0, canvas.width, canvas.height);
 drawBall();
if (x<300 && y==canvas.height-780){
    x += dx
}else if (x >= 300 &&  y < 300){
    y += dx
}else if (x > canvas.width-780 && y >= 300){
    x -= dx
}else if (x <= canvas.width-780 && y > canvas.height-780){
    y -= dx
}
}
setInterval(draw, 10);