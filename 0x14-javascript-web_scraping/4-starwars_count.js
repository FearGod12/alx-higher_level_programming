#!/usr/bin/node
//  prints the number of movies where the character “Wedge Antilles” is present.
//  The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
//  Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
//  You must use the module request

const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body).results;
    let number = 0;

    for (const result of data) {
      for (const cha of result.characters) {
        if (cha.endsWith('/18/')) {
          number++;
        }
      }
    }
    console.log(number);
  }
});
