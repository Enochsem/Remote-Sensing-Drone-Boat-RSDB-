$(document).ready(function () {
    device_id = $("#device_id").val(); 
    notification_count(device_id)  ;  
});

function notification_count(device_id){
    // device_id = $("#device_id").val(); 
    $.ajax({
        type: 'GET',
        url: '/notification_count',
        data: {'device_id': "000" },
        success: (data) => {
          var count =  data['response'];
          document.getElementById("notification_count").innerHTML = count;
          console.log("here here "+count)
        },
  
    });
}