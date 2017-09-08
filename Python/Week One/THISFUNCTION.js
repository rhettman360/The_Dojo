function FBTeam(name, city, color) {
  this.name = name;
  this.city = city;
  this.color = color;
  this.players = [];
}

function player(name, position, number) {
  this.name = name;
  this.position = position;
  this.number = number;
}

var USC = new FBTeam("Trojans", "LA", "Red, Yellow");
USC.players.push(new player("Reggie Bush", "Running Back", "5"));

var SH = new FBTeam("Seahawks", "Seattle", "Blue, White, Green");
SH.players.push(new player("Richard Sherman", "Cornerback", "25"))


console.log(USC, SH);
