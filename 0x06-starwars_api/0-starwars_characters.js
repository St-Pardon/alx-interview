#!/usr/bin/node
const request = require('request');
if (process.argv.length > 2) {
  request(
    `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
    (err, res, body) => {
      if (err) console.log(err);
      const json = JSON.parse(body);
      json.characters.map((item) => {
        request(item, (err, res, body) => {
          if (err) console.log(err);
          const result = JSON.parse(body);
          console.log(result.name);
        });
      });
    }
  );
}
