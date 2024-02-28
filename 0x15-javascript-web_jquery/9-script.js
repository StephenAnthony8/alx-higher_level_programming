/* Fetches from URL and displays the value of Hello */
/* Imported in head tag */

const uRL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.get(uRL, (data, success) => {
  if (success) {
    $('document').ready(() => {
      $('div#hello').html(data.hello);
    });
  }
});
