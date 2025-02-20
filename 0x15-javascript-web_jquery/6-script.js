/* This script updates a header with new content when user click on DIV#update_header */

$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').html('New Header!!!')
  });
});
