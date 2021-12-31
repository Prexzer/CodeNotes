

console.log("Hello, World from JavaScript"); // this is similar to printf


let variable = 5;           // dynamic typing for variables
                            // let is how we declare variables
const forever = "sad";      // Constant variable, can't change it
//alert(forever);           // creates a pop-up on the screen

function sum(a,b)       // one way to declare functions
{
    return a+b;
}

const sub = function(a,b) // the other way to write functions
{
    return a+b;
}

const sub2 = (a,b) => a-b; // same as before just written with the arrow

// call them the same way
sum(1, 2);
sub(2, 1);
