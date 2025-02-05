const express = require("express");
// express:  minimal and fast web framework for Node.js. It helps you build web servers and APIs easily.

const taskApp = express();
const PORT = 3000;

let tasks = ["study!", "update linux server", "create blue/green deployment", "create API", "debug app crash"];

// Start the server
taskApp.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});

// Serve a simple HTML page with tasks
taskApp.get("/", (req, res) => {
    let taskList = "";  // Initialize an empty string

    // Use a traditional for loop to build the HTML list
    for (let index = 0; index < tasks.length; index++) {
        taskList += `<li>${tasks[index]}</li>`;  // Append each task as an <li>
    }

    res.send(`
        <h2>Task List</h2>
        <ul>${taskList}</ul>
    `);
});

/*
  How to run example:
  1. Make sure you install Express.js with ... npm install express
  2. Run this example on CLI ....  node 02-webpage-blog.js
  3. Open  browser and paste: http://localhost:3000

*/

