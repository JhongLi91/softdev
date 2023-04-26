var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById('buttonCircle');
var stopButton = document.getElementById('buttonStop')

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = () => {
  ctx.clearRect(0,0, 1000, 1000);
};

var radius = 0;
var growing = true;

var drawCircle = (e, r) => {
  var circ = c.getBoundingClientRect();
  ctx.beginPath();
  ctx.arc(250, 250, r, 0, Math.PI * 2, true);
  ctx.fillStyle = "blue";
  ctx.fill();
  ctx.stroke();
  ctx.closePath();
}

var drawDot = (e) => {
  if (growing && radius < 250){
    clear();
    drawCircle(e, radius);
    radius+= 1;

    window.requestAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot)
  }

};

var stopIt = (e) => {
  console.log("stopIt invoked...");
  console.log(requestID);
  window.requestAnimationFrame(drawDot)
};

dotButton.addEventListener( "click", drawDot);
stopButton.addEventListener( "click", stopIt);
