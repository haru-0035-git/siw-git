let date = new Date();
document.write(date,"<br>");
let day = ["日","月","火","水","木","金","土"]
document.write(date.getFullYear(),"年",date.getMonth()+1,"月",date.getDate(),"日",day[date.getDay()],"曜日");