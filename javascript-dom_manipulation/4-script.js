const addItemTrigger = document.querySelector('#add_item');
const listElement = document.querySelector('.my_list');

addItemTrigger.addEventListener('click', function () {
  const newItemElement = document.createElement('li');
  newItemElement.textContent = 'Item';
  listElement.appendChild(newItemElement);
});
