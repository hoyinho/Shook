var bet = document.getElementById("bet");
var prize = document.getElementById("prize");
var button = document.getElementById("button");

var win1 = document.getElementById("win1");

var win2 = document.getElementById("win2");
var link = window.location.href;
link = link.substring(link.length-6, link.length);
if (button != null){
    button.addEventListener("click", function(e){
	$.get("/accepted",{link: link},  function(d){});
	location.reload();
    });
}

win1.addEventListener("click", function(e){
    $.get("/win", {whoWin: "1", link: link}, function(d){});
    location.reload();
});

win2.addEventListener("click", function(e){
    $.get("/win", {whoWin: "2", link: link}, function(d){});
    location.reload();
});

