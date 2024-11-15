#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
} else if (isNaN(process.argv[2])) {
  console.error('The movie ID must be a number');
  process.exit(1);
} else {
  const BASE_URL = 'https://swapi-api.alx-tools.com/api';
  const movieId = process.argv[2];

  request(`${BASE_URL}/films/${movieId}`, (error, _, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const characters = JSON.parse(body).characters;

    const promises = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (err, _, data) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(data).name);
          }
        });
      });
    });

    Promise.all(promises)
      .then((characterNames) => {
        characterNames.forEach((name) => console.log(name));
      })
      .catch((err) => console.error(err));
  });
}
