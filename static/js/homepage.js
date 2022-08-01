
$(document).ready(function(){
Swal.fire('Welcome to Remote Sensing')
});



function signup(){
    $.ajax({
        type: 'POST',
        url: '/signup',
        data: {'device_id': device_id},
        success: (data) => {
          console.log("checking " + data['response'][0][3]);
          var graph_data =  data['response'];
          for (let index = 0; index < graph_data.length; index++) {
              if (graph_data[index][2]=="Ph") {
                  ph_sensor.push({x:graph_data[index][4], y:graph_data[index][3]});
              }else if(graph_data[index][2]=="Temperature"){
                  temp_sensor.push({x:graph_data[index][4], y:graph_data[index][3]});
              }else if(graph_data[index][2]=="Turbidity"){
                  tur_sensor.push({x:graph_data[index][4], y:graph_data[index][3]});
              }else if(graph_data[index][2]=="TDS"){
                  tds_sensor.push({x:graph_data[index][4], y:graph_data[index][3]});
              }
          }
  
        
  
        },
  
      });
}