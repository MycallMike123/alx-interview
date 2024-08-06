#!/usr/bin/node

const request = require('request');

// Ensure the correct number of arguments is provided
if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie.id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Define a function to retrieve data from a given URL
const fetchData = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error); 
      } else if (response.statusCode !== 200) {
        reject(new Error(`Request failed, status code: ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body)); 
      }
    });
  });
};

// Fetch movie details and retrieve character data
fetchData(apiUrl)
  .then((movieData) => {
    const characterPromises = movieData.characters.map(
      (characterUrl) => fetchData(characterUrl)
    );
    return Promise.all(characterPromises);
  })
  .then((characters) => { // Display each character's name
    characters.forEach((character) => {
      console.log(character.name);
    });
  })
  .catch((error) => { // Handle any errors encountered
    console.log('Error:', error.message);
  });
