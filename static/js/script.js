$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.not-collapse').on('click', function(e) { e.stopPropagation(); });
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.modal').modal();
  });