
$(function (){

  var $commands = $('#commandhistory');
  $.ajax({
    type: 'POST',
    url: '/commandhistory',
    data: {
      'listtype' : 'top10',
    },
    success: function(commands){
      $.each(commands, function(i, command){

        $commands.append('<tr><td><code>'+ command + '</code></td></tr>')
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

$('bluetooth_button').on('click', function(){
  var pathId = $(this).attr('id');
  var $devices = $('bluetooth_devices')
  $.ajax({
    type: 'POST',
    url: '/bluetoothapi',
    data: {
      "command":pathId
    },
    success: function(devices) {
      console.log('POSTING:' + pathId);
      $devices.empty();
      $.each(devices, function(i, device) {
        $devices.append('<li>' + device + '</li>')
      });

    },
    error: function(){
      console.log('error occured sending' + pathId + 'command');
    }
  })
});

$(function () {
  var $commands = $('#commandhistory');
  var $telemetry = $('#telemetry');
  setInterval(function() {
    $.ajax({
      type: 'POST',
      url: '/commandhistory',
      data: {
        'listtype' : 'top10',
      },
      success: function(commands){
        $commands.empty();
        $.each(commands, function(i, command) {
          $commands.append('<tr><td><code>'+ command + '</code></td></tr>')
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
          $telemetry.append('<tr><td><span class="text-muted text-monospace">' + metric[0] + '</span></td><td><code>' + metric[1]+ '</code></td></tr>')
        });
      }
    });
  }, 500); // 100 is the no of ms to refresh the element
});
