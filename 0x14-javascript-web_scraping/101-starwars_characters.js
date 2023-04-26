#!/usr/bin/node
// computes the number of tasks completed by user id.
// The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
// Only print users with completed task
// You must use the module request
//
const request = require('request');

function check (url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const people = JSON.parse(body).results;

      for (const result of people) {
        for (const film of result.films) {
          if (film.endsWith(process.argv[2] + '/')) {
            console.log(result.name);
          }
        }
      }
    }
    const respons = JSON.parse(body);
    if (respons.next !== null) {
      check(respons.next);
    }
  });
}

const url = 'https://swapi-api.alx-tools.com/api/people/';
check(url);
