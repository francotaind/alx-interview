#!/usr/bin/node
const request = require('request');

//check if movie ID is passed as argument
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_character.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools/api/films/${movieId}`;

//function to get character name from URL using promises
function getCharacterName(url) {
	return new Promise((resolve, reject) => {
		request(url, (error, response, body) => {
			if (error) {
				reject(error);
			} else if (response.statusCode === 200) {
				reject(new Error('API responded with status code ${response.statusCode}'));
			} else {
				const character = JSON.parse(body);
				resolve(character.name);
			}
		});
	});
}
//Main function to fetch film and character data
request(url, async (error, response, body) => {
	if (error) {
		console.error('Error:', error);
		return;
	}

	if (response.statusCode !== 200) {
		console.error('Error: API responded with status code ${response.statusCode}');
		return;
	}

	try {
		const film = JSON.parse(body);
		const characters = film.characters;

		//Fetch all characters names and maintain order
		const characterPromises = characters.map(characterUrl => getCharacterName(characterUrl));
		const characterNames = await Promise.all(characterPromises);

		//Print character names
		characterNames.forEach(name => console.log(name));
	} catch (error) {
		console.error('Error processing data:', error);
	}
});
