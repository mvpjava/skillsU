let taskToDoEveryday = "study!";      // let a variable that can change (block scope)
const MAX_TASKS = 25;    // A constant value

let username = "Bob";
console.log('Your every day task is to: ${taskToDoEveryday}!')      // console is also web based!

/* Process arguments from the command line
   process is a global object in Node.js (does not require importing, like 'console'). I
   Provides information and control over the current Node.js process
*/
let args = process.argv; 

// Get command-line arguments (starting from index 2). first two are Node.js & script paths.
console.log(args); 

// Check if exactly 1 argument is provided (triple === is safer than ==)
if (args.length === 3) {
    console.log(`Your first and only input argument: ${args[2]}`);
} else {
    console.log("Error: Please provide exactly one argument.");
}
