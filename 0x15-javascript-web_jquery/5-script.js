$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append($('<li></li>').text('Item'));
  });
});