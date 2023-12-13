window.addEventListener('load',draw,false);
function draw(){
    var r = 200;
    var x,y;
    var degree = 0;
    var radian;
    var canvas = document.getElementById('cv');
    var context = cv.getContext('2d');
    function loop(){
    degree += 1;
    radian = degree * Math.PI/180;
    x = r * Math.cos(radian) + cv.width/2 + 20;
    y = r * (Math.sin(radian)) + cv.height/2 + 20;
    context.clearRect(0, 0, cv.width, cv.height);
    context.beginPath();
    context.fillStyle = 'red';
    context.arc(x, y, 10, 0, Math.PI*2);
    context.fill();
    context.closePath();
    requestAnimationFrame(loop);
    }
    loop();
    }
draw()

