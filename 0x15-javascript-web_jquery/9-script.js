/* This script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
   and displays the value of hello from that fetch in the HTML tag DIV#hello. */

$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('#hello').text(data.hello)
  });
});
