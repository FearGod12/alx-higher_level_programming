$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    $.each(movies, function (index, movies) {
      $('UL#list_movies').append('<li>' + movies.title + '</li>');
    });
  });
});
