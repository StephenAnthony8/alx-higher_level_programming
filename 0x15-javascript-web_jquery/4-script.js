/* On clicking DIV#toggle_header, toggle between red and green classes */

$('header').addClass('red');
$('div#toggle_header').on('click', () => {
  const hClass = $('header').attr('class');

  /* Ternary operators performing the switch */
  $('header').removeClass((hClass === 'green' ? 'green' : 'red'));
  $('header').addClass((hClass !== 'green' ? 'green' : 'red'));
});
