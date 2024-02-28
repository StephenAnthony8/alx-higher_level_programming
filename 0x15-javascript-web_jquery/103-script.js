/* Says hello in different languages */
/* Language code is in INPUT#language_code */

const uRl = 'https://hellosalut.stefanbohacek.dev/';

function fetchTranslation () {
  const transUrl = uRl + '?lang=' + $('input#language_code').val();
  $.get(transUrl, (data, success) => {
    if (success) {
      $('div#hello').html(data.hello);
    }
  });
}
$(document).ready(() => {
  $('input#btn_translate').click(function () {
    fetchTranslation();
  });

  $('input#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });
});
