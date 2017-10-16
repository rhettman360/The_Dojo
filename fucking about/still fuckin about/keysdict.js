var obj = {'a':1, 'b':2, 'c':3};

for (var letter in obj) {
  console.log(letter);      //This is the key
  console.log(obj[letter]); //This is the value
}
