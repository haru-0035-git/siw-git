function print(local){
    document.write(local,"秒経過","<br>")
}
function disp(){
for (let i = 1;i<=10;i++){
    (function(local){
        timerID=setTimeout(function(){print(local);},i*1000);
    }(i));
}
}
disp()


// var cnt; // カウンタ変数
// function StopW(){
// cnt++;
// document.myForm.display.value =cnt; //カウンターの値をテキストボックスに渡す
// timeoutID = setTimeout("StopW()",1000); // 1秒ごとに自分を呼び出す
// }