function generate(){
    var textBox = document.getElementById("testBox");
    var value = textBox.value;
    var str = "";
    for(var i=0;i<parseInt(value);i++){
        str = str.concat("<div class=\"main\" onclick=\"deleteEle(this)\"></div>");
    }
    var fg = document.getElementById("fg");
    fg.innerHTML = str;
}
function deleteEle(ele){
    var parent = ele.parentNode;
    parent.removeChild(ele);
}