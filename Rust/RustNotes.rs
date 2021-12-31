// rustc fileName.rs            <-- compile command

// mod fileName; // loads in other rust files


// use fileName::functionName to use that function

fn main()
{
    /*
    ===================
    PRINTING TO SCREEN
    ===================
    */

    // prints with a new line
    println!("");
    
    // prints numbers and strings
    println!("{} has {} apples", "Patrick", 3);

    // prints with indexing of args
    println!("{0} has met {1} other {0}s", "Patrick", 3);

    // named args
    println!("{name} has met {num} other {name}s", name = "Patrick", num = 3);

    // printing with conversions
    println!("Binary: {:b}, Hex: {:x}, Octal: {:o}", 10,10,10);

    // placeholder for debug trait
    println!("{:?}", (12, true, "hello"));  // prints a truple here


    /*
    ==========
    VARIABLES
    ==========
    */

    // Variables are immutable by default (CAN'T CHANGE VARIABLE VALUES ONCE SET)
    // block scoped language

    // Primitive types
    // ================

    /*
        Integers: u8, i8, u16, i16, u32, i32, u64, i64, u128, i128 (i = int, u = unsigned, number of bits they take)
        Floats: f32, f64    (f64 is a double in C)
        Boolean: bool
        Characters: char
        Tuples
        Arrays

        let x = 1; <-- i32 by default

        let y = 3.2 <-- f64 by default

        Explicit typing
        let z: i64 = 2000000;

        Unicode for chars

        let emoji = '\u{1F6000}';

        // multiple variables at once
        let (a,b,c) = (1,2,3)

        let (mut a, mut b, mut c) = (1 , 2, 3)

        STRINGS
        =========

        TWO TYPES OF STRINGS
        Primitive str = Immutable fixed-length
        String = Growable, heap-allocated data structiure

        let hello = "hello";                         <-- primitive
        let hello = String::from("Hello");           <-- dynamic   
        let hello = String::with_capacity(10);       <-- creates a string with 10 spaces

        let mut test = String::from("HELLO");        <-- make it mutable
        test.push('!')                               <-- push a char
        test.push_str(" World!")                     <-- push a string

        test.capacity()                              <-- returns number of bytes
        test.is_empty()                              <-- returns true/false
        test.contains()                              <-- returns true/false
        test.replace("World", "Friends")             <-- replaces part of the string

        for word in hello.split_whitespace()         <-- loops through a string printing words ignoring the whitespace
            println!("{}", word);


        let s = String::with_capacity(10);

        s.push('a');
        s.push('b');

        assert_eq!(2, s.len())                       <-- passes
        assert_eq!(10, s.capacity())                 <-- passes

        TUPLES
        ======

        A group of values of different types
        A maximum of 12 elements

        let person: (&str, &str, i8) = ("Patrick", "Mesquita", 100);

        person.0                                     <-- access first item
        person.1                                     <-- access second item

        ARRAYS
        ======

        [type; size]

        let mut arr: [i32; 5];

        arr.len()

        // get part of the array
        let mut arr2: &[i32] = &numbers[0..2]           <-- copies 0, 1

        for x in numbers.iter(){}                       <-- loops through every element

        for x in numbers.iter_mut(){}                   <-- loops through every element **ALLOWS YOU TO CHANGE ELEMENTS

        

        VECTORS
        ========

        Resizeable arrays

        let arr: Vec<i32> = Vec::new();
        or
        let arr: Vec<i32> = vec![]

        let arr: Vec<i32> = [1,2,3,4];              <-- starts the vector with 4 items
        let arr = vec![x; n]                        <-- fills array up with the value x for n number of times

        arr.push()                                  <-- push to the end of vector
        arr.pop()                                   <-- pop off last item


        CONDITIONALS
        ============

        if x > y                                    // we don't need parenthesis () on the condtion
        {
            //statement
        }

        LOOPS
        =====

        loop                                        // no "for" loops, must break on your own
        {
            // statements
        }

        while x > y
        {
            // statements
        }

        POINTERS/REFERENCES
        ===================

        // Rust uses borrowing rather than reference

        let x = String::from("Hello");
        let y = &s;

        // y now owns the new string and x can no longer reference it

        pass-by-reference
        ------------------

        let mut x = 0;

        function(&mut x);

        fn function(variable: &mut i32)
        {
            *x = 10;
        }

        -----------------------------

        This is how you use pointers in Rust

        



        





    */


    let name = "Pat";
    let num = 2;

    // to make a var muttable use "mut"
    let mut temp = 22;

    // Define constant
    // const VARNAME: varType = value; <-- formatting for it
    const ID: i32 = 1;

    // assigning multiple vars
    let (i, j) = ("Hello", 2);

    let z: i64 = std::i64::MAX; // sets to maximum value 

    let flag: bool = 10 < 2;

    



    


}