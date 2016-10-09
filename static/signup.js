var username = document.getElementById("loginUsername");
var password = document.getElementById("loginPassword");
var login = document.getElementById("login");
var error = document.getElementById("error");

var newUser = document.getElementById("newUsername");
var newPass = document.getElementById("newPassword");
var create = document.getElementById("create");

login.addEventListener("click", function(e){
    $.get("/login", {username: username.value, password: password.value}, function(d){
	console.log(d);
	if (d == '"True"'){
	    location.reload();
	}
	else{
	    error.innerHTML = "Account Information is invalid";
	}
    });
});

create.addEventListener("click", function(e){
    $.get("/create", {username: newUser.value, password: newPass.value}, function(d){
	console.log(d.length);
	if (d == '"False"'){
	    error.innerHTML = "Account already exists";
	}
	else{
	    newUser.innerHTML = "";
	    newPass.innerHTML = "";
	    error.innerHTML = "Account made. Log in please";
	}
    });
});
