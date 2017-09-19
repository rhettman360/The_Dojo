function Node(val) {
  this.val = val;
  this. next = null;
}

function Sll() {
  this.head = null;
}

Sll.prototype.add = function (val) {
  mytempNode = new Node(val);
  if(this.head == null){
    this.head = mytempNode;
  } else {
    var cur = this.head;
    while (cur.next != null){
      cur = cur.next;
    }
    cur.next = mytempNode;
  }
  return this
}

Sll.prototype.insert = function (val) {
  newNode = new Node(val);
  newNode.next = this.head;
  this.head = newNode;
  return this
}

Sll.prototype.find = function (x) {
  var temp = this.head;
  var count = 1;
  while (count != x) {
    temp = temp.next;
    count++;
  }
  console.log(temp);
  return temp;
}

Sll.prototype.removeFront = function () {
  var tempfront = this.head
  this.head = this.head.next;
  tempfront = null;
  return this;
};

var ll = new Sll();
ll.add(20).add(30).add(40);
ll.insert(10);
// ll.find(3);
ll.removeFront();
console.log(ll);
