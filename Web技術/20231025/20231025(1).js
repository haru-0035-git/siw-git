let a=5;
let b=6;
let c = (a*b)/2;
let r=8;
document.write(c,'<br>');
document.write('ああああ','<br>');

let s = r*r*Math.PI;
document.write('半径',r,'の面積は',Math.round(s,0),'<br>');

today = new Date();
let christ = new Date(2024,12 - 1,25)
// year = today.getFullYear();
// date = today.getDate();

// document.write(today,'<br>');
// document.write(year,'<br>');
// document.write(date,'<br>');

document.write(today.getTime(),'<br>')

d = (christ.getTime() - today.getTime()) / (24*60*60*1000);
document.write("クリスマスまで",Math.ceil(d),"日です",'<br>')

// bm=3;bd=5; //誕生日
// var today=new Date();
// var birthday=new Date (today.getFullYear(),bm-1,bd);
// d=(birthday.getTime()-today.getTime())/(24*60*60*1000);
// d=Math.ceil(d);
// if(d<0){ //今年の誕生日が過ぎている場合
//  var birthday=new Date(today.getFullYear()+1,bm-1,bd);
//  nd=(birthday.getTime()-today.getTime())/(24*60*60*1000);
//  nd=Math.ceil(nd);
//  document.write("来年の誕生日まで",nd,"日","<br>");
// }
// if(d==0) //今日が誕生日の場合
//  document.write("Happy Birthday!!","<br>");
// if(d>0)
//  document.write("誕生日まであと",d,"日","<br>");

// var dayOfWeek=new Array("日","月","火","水","木","金","土");
// var theDay=new Date();
// theDay.setYear(theDay.getFullYear()+1);
// document.write("来年の今日は、");
// document.write(dayOfWeek[theDay.getDay()]);
// document.write("曜日。")

// 閏年かどうかを調べる関数

// document.write('<head>')
// function isLeapYear(year){
//     // 閏年は、4 で割り切れる。
//     // 例外年の計算をする。100 で割れる年は、閏年ではない。400 で割り切れる年は、閏年。
//     if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)){
//     return true;
//     } 
//     else {
//     return false;
//     }
//     }
//     // 月の最初の曜日を求める関数
// function calcFirstDay(date) {
//     var tmpDate = new Date(); //一時的な保管場所を用意する
//     tmpDate.setTime(date.getTime());
//     tmpDate.setDate(1); // 1 日を求める
//     return tmpDate.getDay(); // 曜日を表す数値を返す
//     }
//     // 月の日数を計算する関数
//     function calcMonthDays(date) {
//      //閏年でない月の日数を配列に格納する
//     var monthDays = new Array (31, 28, 31, 30, 31, 30, 31, 31, 30,31, 30, 31);
//     if (isLeapYear (date.getFullYear())) {
//     monthDays[1] = 29; // 閏年の場合、29 を格納する。
//     }
//     return monthDays[date.getMonth()]; // 月を表す数値を求める返す
//     }
//     // カレンダーを表示する関数
// function dispCal(today, month , firstDay, Days) {
//     document.write(today.getFullYear(), "年");
//     document.write(month+1, "月のカレンダー<BR>");
//     //マス目を、テーブルで用意する
//      document.write("<TABLE>");
//     document.write("<TR><TH>");
//     document.write(" 日 <TH> 月 <TH> 火 <TH> 水 <TH> 木 <TH> 金 <TH> 土 ");
//     document.write("</TR>");
//      document.write("<TR>");
//      var col = 0;
//     //最初の日まで列をとばす
//     for (var i=0; i<firstDay; i++)
//     {
//     document.write("<TD></TD>");
//     col++;
//     }
//     for (var i=1; i<=Days; i++)
//     {
//     document.write("<TD>");
//     if (i == today.getDate()) {
//     var iStr = i.toString().fontcolor("red"); //今日の日付は赤で表示
//     document.write(iStr + "</TD>");
//     }
//     else {
//     document.write(i+"</TD>");
//     }
//     col++;
//     if (col == 7)
//     {
//     document.write("</TR><TR>");
//     col = 0;
//     }
//      }
//      document.write("</TR></TABLE>");
//     }
// document.write('</head>')
   
//     document.write('<CENTER>')
//     var today = new Date();
//     var month = today.getMonth(); // 月を求める
//     var firstDay = calcFirstDay(today); // 最初の日の曜日を求める
//     var Days = calcMonthDays(today); // 月の日数を求める
//     // カレンダーを表示する
//     dispCal(today, month, firstDay, Days);
    
//     document.write('</CENTER>')