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

    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed === true) {
        if (users[todos[i].userId] === undefined) {
          users[todos[i].userId] = 0;
        }
        users[todos[i].userId]++;
      }
    }
    console.log(users);
  }
});
