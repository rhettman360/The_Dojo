function minusOne(x) {
  if (typeof x === 'number') {
    return x-1;
  } else if (x instanceof Array) {
    return x.length - 1;
  }
}
minusOne([1,2,3,4,5,6]);
minusOne(7);
