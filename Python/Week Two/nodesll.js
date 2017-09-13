function Node(val){
  this.val = val;
  this.next = null;
}

function sll(val){
  this.head = null;
  this.add = function(val){
    mytempNode = new Node(val);
    if(this.head == null){
      this.head = mytempNode;
    } else {
      var cur = this.head;
      while (cur.next != null){
        cur = cur.next;
      }
      cur.next = mytempNode
    }
  }
}

a = new sll();
a.add(8);
a.add(9);
a.add(7);
a.add(6);
a.add(5);
console.log(a.head);
console.log(a.head.next);
