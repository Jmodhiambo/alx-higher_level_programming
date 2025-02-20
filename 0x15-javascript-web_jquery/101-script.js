/* This script adds, removes and clears LI elements from a list */

$(document).ready(function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    $('.my_list li:last').remove();
  });

  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
