const helloUrl = 'https://hellosalut.stefanbohacek.com/?lang=fr';

document.addEventListener('DOMContentLoaded', function () {
  const helloElement = document.querySelector('#hello');

  fetch(helloUrl)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      helloElement.textContent = data.hello;
    });
});
