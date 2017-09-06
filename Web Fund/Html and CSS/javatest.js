var arr = [7,42,3,10,20,7,42,3,10,20,7,42,3,10,20,7,42,3,10,20,7,42,3,10,20,7,42,3,10,20,7,42,3,10,20];
var Y = 15
  var count = 0;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] > Y) {
      count++;
    }
  }
  console.log(count);
  console.log(arr.length);