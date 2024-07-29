/*
1. Getting Started
What is JavaScript?
JavaScript is a high-level, interpreted scripting language primarily used for making web pages interactive. It can be used for both client-side and server-side programming.

Setting Up Your Environment
Browser Console: Most browsers have a built-in JavaScript console where you can run code snippets. (Open it with F12 or Ctrl+Shift+I).
Text Editor: Use an editor like VSCode, Sublime Text, or Atom to write and save your JavaScript files (.js).
2. Basic Syntax and Concepts
Hello, World!
*/

console.log('Hello, World!');

/*
console.log(): Outputs data to the console.
Variables Declaration: Use let, const, or var.
*/

let name = 'Jerry';  // mutable variable
const age = 25;      // immutable variable

/*
Data Types
Primitive Types: string, number, boolean, null, undefined, symbol, bigint
*/

let str = 'Hello';        // string
let num = 123;            // number
let isTrue = true;        // boolean
let nothing = null;       // null
let notDefined;           // undefined

/*
OPERATORS
Arithmetic: +, -, *, /, %
Comparison: ==, ===, !=, !==, >, <, >=, <=
Logical: && (and), || (or), ! (not)
CONTROLSTATEMENT        
Conditionals: if, else if, else, switch
*/

let score = 85;

if (score >= 90) {
    console.log('Grade: A');
} else if (score >= 80) {
    console.log('Grade: B');
} else {
    console.log('Grade: C');
}

/*    
Loops: for, while, do...while

*/

for (let i = 0; i < 5; i++) {
    console.log(i);
}

let count = 0;
while (count < 5) {
    console.log(count);
    count++;
}

/*
3. Functions
Defining Functions
*/

function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet('Jerry')); // Outputs: Hello, Jerry!
/*
Arrow Functions
*/

const greeting = (name) => `Hello, ${name}!`;

console.log(greeting('Jerry')); // Outputs: Hello, Jerry!
/*
4. Objects and Arrays
Objects
Definition: Key-value pairs.
*/

let person = {
    name: 'Jerry',
    age: 25,
    greet: function() {
        return `Hello, ${this.name}!`;
    }
};

console.log(person.name); // Jerry
console.log(person.greet()); // Hello, Jerry!
/*
Arrays
Definition: Ordered collection of items.
*/

let fruits = ['Apple', 'Banana', 'Cherry'];

console.log(fruits[1]); // Banana

fruits.push('Date'); // Add item
console.log(fruits); // ['Apple', 'Banana', 'Cherry', 'Date']
/*
5. DOM Manipulation
Selecting Elements
*/

let element = document.getElementById('myElement');
/*
Modifying Content
*/

element.textContent = 'New Content';
/*
Event Handling
*/

element.addEventListener('click', () => {
    alert('Element clicked!');
});

/*
6. Asynchronous JavaScript
Callbacks
*/

function fetchData(callback) {
    setTimeout(() => {
        callback('Data fetched');
    }, 1000);
}

fetchData((data) => {
    console.log(data); // Data fetched
});

/*
Promises
*/

let promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Data fetched');
    }, 1000);
});

promise.then((data) => {
    console.log(data); // Data fetched
});

/*
Async/Await
*/

async function fetchData() {
    let promise = new Promise((resolve) => {
        setTimeout(() => {
            resolve('Data fetched');
        }, 1000);
    });

    let data = await promise;
    console.log(data); // Data fetched
}

fetchData();

/*
7. Advanced Topics
Closures
*/

function createCounter() {
    let count = 0;
    return function() {
        count++;
        return count;
    };
}

let counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2
/*
Modules
ES6 Modules: import and export.
*/


// file1.js


// helloworld.js
// import { greet } from './file1.js';
// console.log(greet('Jerry')); // Hello, Jerry!

/*
Error Handling
*/

try {
    // Code that might throw an error
    let result = riskyOperation();
} catch (error) {
    console.error('An error occurred:', error);
} finally {
    console.log('This will always execute');
}

/*
8. Tools and Libraries
Version Control: Git
Package Managers: npm, yarn
Frameworks/Libraries: React, Angular, Vue.js
Testing: Jest, Mocha
*/

