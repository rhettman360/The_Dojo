function genPokemans() {
  var htmlPkm = "";
  for (var i = 1; i < 152; i++) {
    $.get("http://pokeapi.co/api/v2/pokemon/"+i+"/", function(res) {
      htmlPkm += "<img src="+res.sprites.front_default+">";
      console.log(res.sprites.front_default);
      $('#pokemans').html(htmlPkm);
    }, "json");
  }
  $('#pokemans').html(htmlPkm);
}



$(document).ready(function() {
  genPokemans();
});
