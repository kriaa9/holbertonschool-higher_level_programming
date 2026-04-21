const moviesUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
const moviesListElement = document.querySelector('#list_movies');

fetch(moviesUrl)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    data.results.forEach(function (movie) {
      const movieElement = document.createElement('li');
      movieElement.textContent = movie.title;
      moviesListElement.appendChild(movieElement);
    });
  });
