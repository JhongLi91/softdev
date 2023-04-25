//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ"
    }
    else {
        mode = "rect"
    }
}

var drawRect = function(e) {
    var rect = c.getBoundingClientRect();
    var mouseX = e.x - rect.left; //gets X-coor of mouse when event is fired
    var mouseY = e.y - rect.top; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillRect(mouseX, mouseY, 20, 21);
}

var drawCricle = (e) => {
  var circ = c.getBoundingClientRect();
  var mouseX = e.clientX - rect.left;//gets X-coor of mouse when event is fired
  var mouseY = e.clientY - left.top;//gets Y-coor of mouse when event is fired
  console.log("mouseclick registered at ", mouseX, mouseY);
  ctx.beginPath();
  ctx.arc(mouseX, mouseY, 50, 0, MATH.PI * 2, true);
  ctx.fillStyle = "orange";
  ctx.fill();
  ctx.closePath();
}

var draw = (e) => {
	 switch(mode){
		   case "rect":
			    drawRect(e);
			    break;
		   case "circ":
          drawCircle(e);
			    break;
		   default:
			    break;
	 }
}

var wipeCanvas = () =>{
    ctx.clearRect(0,0, 10000, 10000);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
