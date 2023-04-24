/*
   your PPTASK:

   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.

    		Write with your future self or teammates in mind.

    		If you find yourself falling out of flow mode, consult
    		other teams
    		MDN

   A few comments have been pre-filled for you...

   (delete this block comment once you are done)
*/

// Jian Hong Li
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-019t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
        };

console.log(o)
var addItem = function(text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
var fib = function(n){
    if (n == 0){
	    return 0;
    }
    if (n == 1){
      return 1;
    }
    return fib(n-1) + fib(n-2);
};
 // FIB
var fac = function(n){
    if (n == 1){
	     return 1;
    }
    return n * fac(n-1);
};
// FAC
var gcd = function (x, y) {
  while(y) {
    var t = y;
    y = x % y;
    x = t;
  }
  return x;
};
// GCD

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  retVal = param1 * param2;
  return retVal;
};

const myInput = document.getElementById('my-input');
const myInput2 = document.getElementById('my-input2');
const myInput3 = document.getElementById('my-input3');
const myButton = document.getElementById('my-button');
const myButton2 = document.getElementById('my-button2');
const myButton3 = document.getElementById('my-button3');
const content = document.getElementById('FIB');
const content2 = document.getElementById('FACT');
const content3 = document.getElementById('GCD');

myButton.addEventListener('click', function(event) { // adjusting the functions to avoid repition
  const myInputValue = myInput.value;

  content.innerHTML = fib(myInputValue);
}

myButton2.addEventListener('click', function(event) {
  const myInputValue = myInput2.value;

  content2.innerHTML = fact(myInputValue);
}

myButton3.addEventListener('click', function(event) {
  const myInputArray = myInput3.value.split(" ");

  content3.innerHTML = gcd(myInputArray[0], myInputArray[1]);
}
