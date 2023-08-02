$(document).ready(function() {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, status){
      const movies = data.results;
      movies.forEach(element => {
        $('#list_movies').append('<li>' + element.title + '</li>');
      });  
    });

  });
