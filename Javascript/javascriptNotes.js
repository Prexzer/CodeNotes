/*
    Data types in JavaScript --> undefined, null, boolean, string, bigInt, number, object

    "use strict"; --> enables strict mode for the code

    Declare a variable
    ------------------
    var cool;
    
    --> variables can be numbers, chars, strings, etc.. (dynamically typed)

    let otherVar; *ALWAYS USE LET

    why? let allows only one declaration.
    !--> The difference between let and var is, var allows for you to overwrite variable declaration(very bad)

    const COOL;              <-- creates a read only variable

    ***Objects assigned const type are still mutable!
        Ex: const s = [5, 6, 7];
            s[0] = 1;
        prints -> [1, 6, 7]

    Object.freeze(objectName) <-- freezes an object, preventing it from being mutated.


    Print to screen
    ---------------
    console.log();


    Strings
    -------
    var stringy = 'this is valid';
    var stringie = "this is valid";

    --> Strings can be inclosed in double quotes or single quotes(must end with the same starting)
        --> single quotes for strings are useful for when the string contains double quotes and you can not use escape('\') character

    stringy = "how to combine" + "strings together";

    stringy.length; --> returns length (Note, strings are objects and length seems to be a accessing a field)

    stringy[1]; --> accesses letter in second index

    STRINGS ARE IMMUTABLE!
        stringy = "Dog"
        stringy[0] = 'L'

        // stringy will still be Dog, only way to change a string is to reassign the entire string 


    == operator lets you compare numbers and strings. Ex: 3 == '3' or 3 == "3" will both return true
    === used for strict comparsions, no type conversion
    !== strict not equal to

    typeof --> returns the variable type as a string. Ex "typeof 3" returns the string "number"

    do
    {

    } while();          <-- do while LOOP

    Math.random()       <-- returns random number between 0 and 1
    Math.floor()        <-- rounds a number down

    parseInt(string)          <-- parses a string and returns it's integer value
    parseInt(string,radix)    <-- parses a string and returns it's integer value based on the radix(base conversion 2 - 32) USEFUL FOR BINARY

    deconstruct
    ------------
    const user = { name: 'John Doe', age: 34 };
    const name = user.name;
    const age = user.age;

    -->instead do

    const {name, age} = user;

    const {name: person, age: years} = user;  <-- person = user.name, years = user.age

    const {johnDoe:{age, email}} = user;      <-- pulling from an object within an object

    const[a,b,,, c] = [1, 2, 3, 4, 5, 6];

    --> This deconstructs the array into three values, a = 1, b = 2, c = 5

    const[a, b, ...arr] = [1, 2, 3, 4, 5, 6];

    --> collects the rest terms into a seperate array. (a = 1, b = 2, arr = [3,4,5,6])

    [b , a] = [a, b];


    Objects
    ========

    let dog =
    {
        name: "bob",
        legs: 5,
        friends: [],
        "Owner name": "steve"
    };

    javascript will typecast every no string to a string --> legs: 5 becomes "legs": "5";

    ALTERNATE OBJECT ACCESS
    -----------------------
    dog.name                <-- regular access
    dog["Owner name"]       <-- used to access the string with a space in it. ***(Useful for look up too)
    
    You can add object properties after delcaring them.
    dog.bark = "woof";        <-- will create a new bark property for dog.

    delete dog.bark           <-- deletes a property

    dog.hasOwnProperty()      <-- checks for property

    let dog =
    [
        {
            name: "bob",
            legs: 5,
            friends: [],
            "Owner name": "steve"
        },

        {
            name: "sally",
            legs: 7,
            friends: [bob, fred],
            "Owner name": "pat"
        },
    ]       
    <-- creates an object array

    dog[1].friends[1]       <-- accessing an array inside an array.
        
    var myStorage = 
    {
        "car": 
        {
            "inside": 
            {
                "glove box": "maps",
                "passenger seat": "crumbs"
            },
            "outside": 
            {
                "trunk": "jack"
            }
        }
    };

    var gloveBoxContents = myStorage.car.inside["glove box"]; <-- Accessing an object inside an object


    Array
    =====

    var arr = ["This", 1]                 <-- can store strings and nums into same array
                [["hi", 1], ["bye", 200]]   <-- Multi-dimensional array
            
    Multi-dimensional
    ------------------
    arr.length                            <-- gives the number of arrays inside
    arr[i].length                         <-- length of that array inside

    arr.push()                            <-- pushes into the end of array
    arr.pop()                             <-- pops at the end of the array and returns value
    arr.shift()                           <-- pops the first item of array and returns value
    arr.unshift()                         <-- pushes into the start of the array

    

    Function
    ========

    function functionName()               <-- does not need a type
    {
    }

    const varName = () => "return";       <-- assigns fuction to var name, returns the string "return";
    const varName = () => {
        .... code.....
    }

    const varName = (name = "Anonymous") => "hello " + name;        <-- default arg if not arg is passed in 

    const varName = (...args) => return   <-- allows multiple args(spread operator)
    args.length                           <-- how many args passed in

    const varName = ({name, age}) => return     <-- can deconstruct an object when its passed in as a parameter

    


    








*/