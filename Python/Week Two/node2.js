function Node(val){
  this.val = val;
  this.next = null;
}

function sll(val) {
  this.head = null;
  this.add = function(val) {
    mytempNode = new Node(val);
    if(this.head == null){
      this.head = mytempNode;
    } else {
      var cur = this.head;
      while (cur.next != null) {
        cur = cur.next;
      }
      cur.next = mytempNode
    }
  }
}

sll = new sll();
sll.add(1);
sll.add(2);
sll.add(3);
sll.add(4);
console.log(sll.head);
