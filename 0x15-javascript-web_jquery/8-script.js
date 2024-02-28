/* Fetches & lists all movie titles using the URL */
/* inserted into UL#list_movies */
const uRl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(uRl, (data, success) => {
  if (success) {
    const movieList = data.results;
    for (const movie of movieList) {
      $('ul#list_movies').append('<li>' + movie.title + '</li>');
    }
  }
});
