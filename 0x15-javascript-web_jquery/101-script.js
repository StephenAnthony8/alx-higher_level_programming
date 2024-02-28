/* when a user clicks:
    DIV#add_item: add item to list
    DIV#remove_item: remove item from list
    DIV#clear_list: remove all elements */
/* imported in head tag */
$('document').ready(() => {
  /* add item */
  $('div#add_item').click(() => {
    $('ul.my_list').append('<li>Item</li>');
  });

  /* remove item */
  $('div#remove_item').click(() => {
    $('ul.my_list').children().last().remove();
  });

  /* clear list */
  $('div#clear_list').click(() => {
    $('ul.my_list').empty();
  });
});
