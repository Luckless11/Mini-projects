let clicks=0;
let clickPower=1;
let cost=15;
let level=0;

document.getElementById("up").innerHTML = "Click here to gain 1 Click power! Cost: " + cost + " Clicks";     
document.getElementById("b").innerHTML = "Click here to gain " + clickPower + " Clicks!";
document.getElementById("clikcs").innerHTML = "Hello person! You have " + clicks + " Clicks!";

function addclicks() {
	clicks += clickPower;
	document.getElementById("clikcs").innerHTML = "Hello person! You have "+ clicks +" Clicks!";
}

function addclickpower(num) {
	clickPower += num;
	level += 1;
	clicks -= cost
	console.log(cost)
	cost = cost * 1.5 ** level;
	console.log(cost)
	document.getElementById("clikcs").innerHTML = "Hello person! You have " + clicks + " Clicks!";
	document.getElementById("b").innerHTML = "Click here to gain " + clickPower + " Clicks!";
	document.getElementById("up").innerHTML = "Click here to gain 1 Click power! Cost: " + cost + " Clicks";
}
