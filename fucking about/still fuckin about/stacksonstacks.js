function Stack(){
  this.contents = [];
  console.log(this.contents);
}

Stack.prototype.add = function (val) {
  this.contents.push(val);
}

Stack.prototype.remove = function () {
  return this.contents.pop();
};

var theStack = new Stack();
theStack.add(6);
theStack.add(6);
theStack.remove
