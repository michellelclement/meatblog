$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
  });

$('.upload_form').append($.cloudinary.unsigned_upload_tag("meatblog", 
  { cloud_name: 'du2vwqykf' }));
