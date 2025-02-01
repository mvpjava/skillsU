const express = require("express");
// express:  minimal and fast web framework for Node.js. It helps you build web servers and APIs easily.

const taskApp = express();
const PORT = 3000;

let tasks = ["study!", "update linux server", "create blue/green deployment", "create API", "debug app creash"];

// Start the server
taskApp.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});

// Middleware to parse POST request data (important for forms)
taskApp.use(express.urlencoded({ extended: true }));  // Parse URL-encoded data
// Serve a simple HTML page with tasks
taskApp.get("/", (req, res) => {
    let taskList = "";  // Initialize an empty string

    // Use a traditional for loop to build the HTML list
    for (let index = 0; index < tasks.length; index++) {
        taskList += `<li>${tasks[index]}</li>`;  // Append each task as an <li>
    }

    // Send the HTML page with task list and form
    res.send(`
        <h2>Task List</h2>
        <ul>${taskList}</ul>
        <h3>Add a New Task</h3>
        <form method="POST" action="/add">
            <input type="text" name="task" required>
            <button type="submit">Add Task</button>
        </form>
    `);
});

// Route to handle adding a new task
taskApp.post("/add", (req, res) => {
    const newTask = req.body.task;  // Get task from the form input
    tasks.push(newTask);  // Add new task to the task list
    res.redirect("/");  // Redirect to the main page to show updated tasks
});


// How do we remove tasks ponce done?