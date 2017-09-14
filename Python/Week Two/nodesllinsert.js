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


var ll = new Sll();
ll.add(20).add(30);
ll.insert(10);
console.log(ll);
