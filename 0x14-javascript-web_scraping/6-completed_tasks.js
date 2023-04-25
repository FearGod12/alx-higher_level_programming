#!/usr/bin/node
// computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only print users with completed task
// You must use the module request
//
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const users = {};
    for (let j = 1; j <= 10; j++) {
      users[j] = 0;
    }
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        users[todos[i].userId] += 1;
      }
    }
    console.log(users);
  }
});
