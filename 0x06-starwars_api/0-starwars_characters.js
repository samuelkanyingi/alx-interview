#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Create a function to fetch and print character names
  function fetchCharacterName (url) {
    return new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  }

  // Fetch and print all character names sequentially
  (async () => {
    for (const url of characterUrls) {
      try {
        const name = await fetchCharacterName(url);
        console.log(name);
      } catch (err) {
        console.error('Error fetching character:', err);
      }
    }
  })();
});
