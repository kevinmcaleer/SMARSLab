
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
  var $telemetry = $('#telemetry');
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
    $.ajax({
      type: 'POST',
      url: '/metricsapi',
      data: {
        "metric": "telemetry"
      },
      success: function(metrics){
        $telemetry.empty();
        $.each(metrics, function(i, metric) {

          // console.log(metric)
          $telemetry.append('<li>' + metric[0] + ' ' + metric[1]+ '</li>')
        });
      }
    });
  }, 50); // 100 is the no of ms to refresh the element
});
