var bet = document.getElementById("bet");
var button = document.getElementById("button");
var prize = document.getElementById("prize");
var link = document.getElementById("newLink");

button.addEventListener("click", function(e){
    $.get("/makeBet", {bet:bet.value, prize: prize.value} , function(d){
	d = d.substring(1,d.length - 1);
	link.innerHTML = "Send this link to your friend:     " + window.location.href+ d;
    });
});

	 
