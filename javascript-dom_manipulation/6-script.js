const characterUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const characterElement = document.querySelector('#character');

fetch(characterUrl)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    characterElement.textContent = data.name;
  });
