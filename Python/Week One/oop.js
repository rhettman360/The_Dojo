var ray = {name:"Rayquaza",
           type:["Dragon", "Flying"],
           attack:["Fly", "Hyper Voice", "Outrage", "Beam"]
}

function createRayquaza(name, type, attack) {
  this.name = name;
  this.type = type;
  this.attack = attack;
}

var l1 = new createRayquaza("Rayquaza", ["Dragon", "Flying"], ["Fly", "Hyper Voice", "Outrage", "Beam"])

console.log(l1);
