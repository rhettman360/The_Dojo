function remDup(str) {
  var newStr = "";
  for (var x = 0; x = str.length; x++) {
    for (var i = 0; i <= newStr.length; i++){
      if (newStr[i] != str[x]){
        console.log(x);
        newStr = newStr + newStr[i];
      }
    }
  }
  console.log(newStr);
}
remDup("hello my name is rhett");
