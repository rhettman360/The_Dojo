function theFunction(n) {
  console.log(n);
}
// var theFunction = "not a function"
function isFunction(x, y) {
  if (typeof x === 'function') {
    x(y);
    console.log("Is a function");
  } else {
    console.log("Not a function");
  }
}

isFunction(theFunction, "test")
