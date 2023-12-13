// for (x=0; x<=180;x=x+10){
//     s=Math.sin(x*Math.PI/180);
//     document.write(x,',',s,'<br>');
// }

// function spc(n){
//     s='';
//     for (i=0;i<n;i++)
//     s=s+'　';
//     return s;
// }


// document.write("<pre>")
// document.write('\t-1.........+........0.........+..........1<br><br>');
// for (x=0;x<=360;x=x+20){
//     ts=10*Math.sin(x*Math.PI/180)+10;
//     document.write(x,'\t',spc(ts),'*<br>')
// }
// document.write('</pre>')

let d = 0
let ki = 0
let kyo = 0
for (x=0;x<30;x++){
    let num = (Math.floor(Math.random()*10));
    if (num % 3 == 0){
        document.write('大吉','<br>');
        d = d +1
    }
    else if(num % 3 == 1){
        document.write('吉','<br>');
        ki = ki + 1
    }
    else if(num % 3 == 2){
        document.write('凶','<br>');
        kyo = kyo + 1
    }
}

document.write('大吉:',d,'回','<br>','吉',ki,'回','<br>','凶',kyo,'回')

document.fgColor = 'magenta'
document.bgColor = 'cyan'