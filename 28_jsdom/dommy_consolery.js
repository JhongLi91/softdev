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
      console.log(items[i].classList)
    if (i%2==0){
      items[i].classList.remove('blue');
      items[i].classList.remove('green');
      items[i].classList.add('red');
    } else {
      items[i].classList.remove('red');
      items[i].classList.remove('green');
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB

var fib = function(n){
  if (n < 2) return n;
  return fib(n - 2) + fib(n - 1);
};

// FAC

function fact(n){
    if(n <= 1){
        return 1;
    }
    else{
        return n * fact(n-1);
    }

}
// GCD

function gcd(x, y){
  while(y) {
    var temp = y;
    y = x % y;
    x = temp;
  }
  return x;
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
  // body
  return retVal;
};

var fibButton = document.getElementById('fib')
var facButton = document.getElementById('fac')
var gcdButton = document.getElementById('gcd')

var a = 10
var b = 37

var buttonArray = []
for (let i = 0; i < 10; i++){
  buttonArray[i] = document.getElementById('a' + i)
}

for (let i = 0; i < 10; i++){
  buttonArray[i].addEventListener('click', () => {
    var thing = document.getElementById("valueOfA");
    a = 10 * a + i
    thing.innerHTML = "value of the input: " + a
  })
}

var backspace = document.getElementById("backspace")
backspace.addEventListener('click', () => {
  var thing = document.getElementById("valueOfA");
  a = Math.trunc(a / 10)
  thing.innerHTML = "value of the input: " + a
})

fibButton.addEventListener('click', () => {
  var thing = document.getElementById("calculatorNans");
  thing.innerHTML = "the " + a + "th term of the fibonacci sequence is " + fib(a)
})
facButton.addEventListener('click', function() {
  var thing = document.getElementById("calculatorNans");
  thing.innerHTML = "factorial of " + a + " is " + fac(a)
})
gcdButton.addEventListener('click', function() {
  var thing = document.getElementById("calculatorNans");
  thing.innerHTML = "gcd of " + a + " and " + b + " is " + gcd(a,b)
})
