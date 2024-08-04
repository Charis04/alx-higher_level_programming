#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to fetch data. Status code: ${response.statusCode}`);
  } else {
    const films = JSON.parse(body).results;
    let charCount = 0;
    for (const film of films) {
      if (film.characters.includes(character)) {
        charCount++;
      }
    }
    console.log(charCount);
  }
});
