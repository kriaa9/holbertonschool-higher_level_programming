const redHeaderTrigger = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

redHeaderTrigger.addEventListener('click', function () {
  headerElement.style.color = '#FF0000';
});
