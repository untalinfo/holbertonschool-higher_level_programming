$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (resp) {
    $('DIV#hello').text(resp.hello);
  });
});
