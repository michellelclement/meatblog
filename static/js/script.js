$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.modal').modal();
  });

if (document.getElementById('date_added') !== undefined || document.getElementById('date_added') !== null) {
  document.getElementById('date_added').value = Date();
}
  
