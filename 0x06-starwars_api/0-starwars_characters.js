#!/usr/bin/node
const request = require('request');
const BASE_URL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  request(`${BASE_URL}/films/${process.argv[2]}/`, (error, _, body) => {
    if (error) {
      console.log(error);
    }
    const characters = JSON.parse(body).characters;
    const promises = characters.map(characterUrl =>
      new Promise((resolve, reject) => {
        request(characterUrl, (err, _, data) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(data).name);
        });
      }));
    Promise.all(promises)
      .then(characterNames => console.log(characterNames.join('\n')))
      .catch(err => console.log(err));
  });
}
