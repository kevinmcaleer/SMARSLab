
$(function (){

  var $commands = $('#commandhistory');
  $.ajax({
    type: 'GET',
    url: '/commandhistory',
    success: function(commands){
      $.each(commands, function(i, command){
        $commands.append('<li>'+ command + '</li>')
      });
      console.log('success', commands);
    }
  });
});

$('.control_button').on('click', function() {
  var controlId = $(this).attr('id');
  $.ajax({
    type: 'POST',
    url: '/controlapi',
    data: {
      "command": controlId
    },
    success: function() {
      // window.status = controlId

      console.log('POSTING: ' + controlId);
    },
    error: function() {
      // alert('error occured sending up command')
      console.log('error occured sending ' + controlId +' command');
    }
  })
});

$(function () {
  var $commands = $('#commandhistory');
  setInterval(function() {
    $.ajax({
      type: 'GET',
      url: '/commandhistory',
      success: function(commands){
        $commands.empty();
        $.each(commands, function(i, command) {
          $commands.append('<li>' + command + '</li>')
        });
      }
    });
  }, 100); // 100 is the no of ms to refresh the element
});
