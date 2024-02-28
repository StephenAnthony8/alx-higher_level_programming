/* Says hello in different languages */
/* Language code is in INPUT#language_code */

const uRl = 'https://hellosalut.stefanbohacek.dev/';

$('window').ready(() => {
  $('input#btn_translate').click(() => {
    const transUrl = uRl + '?lang=' + $('input#language_code').val();
    $.get(transUrl, (data, success) => {
      if (success) {
        $('div#hello').html(data.hello);
      }
    });
  });
});
