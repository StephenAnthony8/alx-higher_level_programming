/* Fetches character name from given URL & display in DIV#character */
const uRl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(uRl, (data, success) => {
  if (success) {
    const characterName = data.name;
    $('div#character').html(characterName);
  }
});
