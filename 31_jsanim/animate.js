var c = document.getElementById("slate"); // GET CANVAS
var dotButton = document.getElementById('buttonCircle');
var stopButton = document.getElementById('buttonStop')

var ctx = c.getContext("2d");

ctx.fillStyle = "orange";

var requestID;

var clear = () => {
  ctx.clearRect(0,0, 10000, 10000);
};

var radius = 0;
var growing = true;

var drawCircle = (e, r) => {
  var circ = c.getBoundingClientRect();
  console.log("mouseclick registered at ", mouseX, mouseY);
  ctx.beginPath();
  ctx.arc(500, 500, r, 0, Math.PI * 2, true);
  ctx.fillStyle = "orange";
  ctx.fill();
  ctx.stroke();
  ctx.closePath();
}

var drawDot = (e) => {
  while (growing){
    clear();
    drawCircle(e, radius)
    radius++
  }
};

var stopIt = (e) => {
  console.log("stopIt invoked...");
  console.log(requestID);

};

dotButton.addEventListener( "click", drawDot);
stopButton.addEventListener( "click", stopIt);
