var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
//四角形の描写
// ctx.beginPath();
// ctx.rect(20, 40, 50, 50);
// ctx.fillStyle = "#FF0000";
// ctx.fill();
// ctx.closePath();

//線の描写
// ctx.beginPath();
// ctx.moveTo(50, 50);
// ctx.lineTo(250,250)
// ctx.stroke();

//三角形の描写
// ctx.beginPath();
// ctx.moveTo(150,50);
// ctx.lineTo(250,200);
// ctx.lineTo(50,200);
// ctx.closePath();
// ctx.stroke();

//円の描写
// ctx.beginPath();
// ctx.arc(450,450,200,0, Math.PI*2 ,true);
// ctx.closePath();
// ctx.strokeStyle = "#1874CD";
// ctx.lineWidth = 3;
// ctx.stroke();

// ctx.beginPath();
// ctx.arc(500,450,150,0, Math.PI*2 ,true);
// ctx.closePath();
// ctx.strokeStyle = "#1874CD";
// ctx.lineWidth = 3;
// ctx.stroke();

// ctx.beginPath();
// ctx.arc(550,450,100,0, Math.PI*2 ,true);
// ctx.closePath();
// ctx.strokeStyle = "#1874CD";
// ctx.lineWidth = 3;
// ctx.stroke();

// ctx.beginPath();
// ctx.arc(600,450,50,0, Math.PI*2 ,true);
// ctx.closePath();
// ctx.strokeStyle = "#1874CD";
// ctx.lineWidth = 3;
// ctx.stroke();

ctx.beginPath();
ctx.moveTo(450,50);
ctx.lineTo(550,200);
ctx.lineTo(350,200);
ctx.fillStyle = '#006400'
ctx.fill()
ctx.closePath();
ctx.stroke();

ctx.beginPath();
ctx.arc((550+350)/2,280,80,0, Math.PI*2 ,true);
ctx.closePath();
ctx.stroke();


ctx.beginPath();
ctx.moveTo(550,360);
ctx.lineTo(550,480);
ctx.lineTo(350,480);
ctx.lineTo(350,360);
ctx.closePath();
ctx.stroke();

ctx.beginPath();
ctx.moveTo((550+350)/2, 20);
ctx.lineTo((550+350)/2,700);
ctx.strokeStyle = "#1874CD";
ctx.stroke();
