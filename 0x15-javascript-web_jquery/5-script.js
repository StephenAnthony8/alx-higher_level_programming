/* add li item on DIV#add_item click */
$('div#add_item').on('click', () => {
  $('ul.my_list').append('<li>Item</li>');
});
