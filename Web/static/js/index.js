// Side bar
$(document).ready(function () {
    // sidebar
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});



$(document).ready(function () {
    // floating button to toggle sidebar
    $('#floating_button').on('click', function () {
        console.log("clicked")
        $('#sidebar').toggleClass('active');
    });
});

function getTimestamp () {
    const pad = (n,s=2) => (`${new Array(s).fill(0)}${n}`).slice(-s);
    const d = new Date();
    return `${pad(d.getFullYear(),4)}-${pad(d.getMonth()+1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
}

var date = getTimestamp();

var notification_Title = "Notification "+date

var Ph_Sensor_Title = "Ph Sensor "+date;
var Turbidity_Title = "Turbidity Sensor "+date;
var TDS_Title = "TDS Sensor "+date;
var Temperature_Title = 'Temperature Sensor '+date;





$(document).ready(function () {
     // notification Tables
     $('#notification_table').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                title: notification_Title
            },
            {
                extend: 'pdfHtml5',
                title: notification_Title
            }
        ]
    } );
});


$(document).ready(function () {
     // Ph_Sensor Tables
     $('#Ph_Sensor').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                title: Ph_Sensor_Title
            },
            {
                extend: 'pdfHtml5',
                title: Ph_Sensor_Title
            }
        ]
    } );

    // tds_sensor
    $('#tds_sensor').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                title: TDS_Title
            },
            {
                extend: 'pdfHtml5',
                title: TDS_Title
            }
        ]
    } );


    // turbidity_sensor
    $('#turbidity_sensor').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                title: Turbidity_Title
            },
            {
                extend: 'pdfHtml5',
                title: Turbidity_Title
            }
        ]
    } );


    // temperature_sensor
    $('#temperature_sensor').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                title: Temperature_Title
            },
            {
                extend: 'pdfHtml5',
                title: Temperature_Title
            }
        ]
    } );


});



let ph_line = null;
let temperature_line = null; 
let tubidity_bar = null;
let pie = null;

var yaxis =[];
// Ph graph
$(document).ready(function(){
    // var yaxis = [{x:'2016-12-25', y:20}, {x:'2016-12-26', y:10}];
    const data = {
        datasets: [{label: 'Ph Sensor',fill: false,lineTension: 0,
        backgroundColor: "rgba(0,0,205,1.0)",
        borderColor: "rgba(0,0,255,0.1)",
        data: yaxis}]
    }
    
    const config = {
        type: "line",
        data: data,
        options: {}
    }
    if(ph_line != null){ph_line.destroy();}
    // rendering the chart
     ph_line = new Chart(document.getElementById('ph'),config);
     

});


var temperature_coordinate = [];
$(document).ready(function(){

    data = {
        datasets: [{label: 'Temperature',fill: false,lineTension: 0,
        backgroundColor: "rgba(0,255,0,1.0)",
        borderColor: "rgba(0,255,0,0.1)",
        data:temperature_coordinate}]
    },

    config =  {
        type: "line",
        data: data,
        options: {legend: {display: false} }
        }

    if(temperature_line != null){temperature_line.destroy();}
    

    temperature_line = new Chart($("#temperature"), config);

});





tubidity_coordinate = [];
// bar graph
$(document).ready(function(){
    const ctx = document.getElementById('turbidity');

    if(tubidity_bar!=null){tubidity_bar.destroy();} //prevent destroy error

    data =  {
        datasets: [{
            label: 'Turbidity',
            data: tubidity_coordinate,
            backgroundColor: ['rgba(255, 99, 132, 0.2)'],
            borderColor: ['rgba(255, 99, 132, 1)'],
            borderWidth: 1
        }]
    }

    config = {
        type: 'bar',
        data: data,
        options: {scales: { y: { beginAtZero: true} }  }
    }
    tubidity_bar =  new Chart(ctx, config);
});



pie_coordinate = [];
// pie chart
$(document).ready(function(){
    const tag = document.getElementById('tds');

    const data = {
        datasets: [{
          label: 'TDS Sensor',
          data: pie_coordinate,
          backgroundColor: ['rgb(255, 99, 132)','rgb(255, 99, 2)'],
          hoverOffset: 4
        }]
      };

    var config = {type: 'bar', data: data}

    if(pie!=null){pie.destroy(); } //prevent destroy errorpi

    pie = new Chart(tag, config);

});



///////////// combo_graph /////////////
let combo_graph = null;
var ph_sensor = [];
var tds_sensor = [];
var temp_sensor = [];
var tur_sensor = [];

$(document).ready(function(){
    // var yaxis = [{x:'2016-12-25', y:20}, {x:'2016-12-26', y:10}];
    const data = {
        datasets: [{
            type: "line",
            label: 'Ph',fill: false,lineTension: 0,
            backgroundColor: "rgba(0,0,205,1.0)",
            borderColor: "rgba(0,0,255,0.1)",
            data: ph_sensor},
            {
                type: 'line',
                label: 'TDS',
                data: tds_sensor,
                backgroundColor: "rgba(0,220,205,1.0)"
            },
            {
                type: 'line',
                label: 'Temperature',
                data: temp_sensor,
                backgroundColor: "rgba(0,205,0,1.0)"
            },
            {
                type: 'line',
                label: 'Turbidity',
                data: tur_sensor,
                backgroundColor: "rgba(222,0,0,1.0)"
            }
        ]
    }
    
    const config = {
        // type: "line",
        data: data,
        options: {}
    }
    if(combo_graph != null){combo_graph.destroy();}
    // rendering the chart
    combo_graph = new Chart(document.getElementById('combo_graph'),config);
     

});





// update charts on dashboard
function updateGraphData(chart, data) {
    // chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}


function getdate () {
    const pad = (n,s=2) => (`${new Array(s).fill(0)}${n}`).slice(-s);
    const d = new Date();
    return `${pad(d.getFullYear(),4)}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
}


var graph_date = getdate();

// load data from api on ajax call
const baseURL = "http://127.0.0.1:5000"



$(document).ready(function(){
    console.log(baseURL+"hehe");
    device_id = $("#device_id").val();
    $.ajax({
      type: 'GET',
      url: '/all_graph_data',
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

        // graph_data.forEach(element => {
        //     yaxis.push({x: graph_date, y: element[3]}, {x: element[3], y: 10});
        // });

        combo_graph.data.datasets.forEach((dataset) => {
            dataset.data.push(ph_sensor);
            dataset.data.push(temp_sensor);
            dataset.data.push(tur_sensor);
            dataset.data.push(tds_sensor);
        });
        combo_graph.update();

      },

    });

//     // from flask_cors import CORS
//     console.log("zzzzzz")
});


// Shijou Saikyou no Daimaou, Murabito A ni Tensei suru Episode 9 English Subbed at gogoanime
function plot_graph(sensor_type, chart, coordinates){
    device_id = $("#device_id").val();
    $.ajax({
        type: 'GET',
        url: '/get_graph_data',
        data: {'device_id': device_id, 'sensor_type': sensor_type },
        success: (data) => {
          graph_data =  data['response'];
          for (let index = 0; index < graph_data.length; index++) {
            coordinates.push({x:graph_data[index][4], y:graph_data[index][3]}, {x:'green',y:54});
          }
  
          updateGraphData(chart, coordinates);
          // graph_data.forEach(element => {
          //     coordinates.push({x:element[3], y:graph_date})
          // });
          
          //for dashboard cards
          var last_element = graph_data[graph_data.length-1][3];
          set_card_data(sensor_type, last_element);

        },
  
    });
}


$(document).ready(function(){
    plot_graph("Ph",ph_line,yaxis); //Ph Graph
    plot_graph(sensor_type="Temperature", chart=temperature_line, coordinates=temperature_coordinate); //temperature Graph
    plot_graph(sensor_type="Turbidity", chart=tubidity_bar, coordinates=tubidity_coordinate); //Turbidity Graph
    plot_graph(sensor_type="TDS", chart=pie, coordinates=pie_coordinate); //TDS Graph

    // combo graph
    


});


function set_card_data(sensor_type,last_element){
    if (sensor_type == "Ph") {
        $('#Ph_value').html(last_element);
        console.log('hereyyyy' + last_element);
    }else if(sensor_type == "Turbidity"){
        $('#Turbidity_value').html(last_element + " NTU");
    }else if(sensor_type == "Temperature"){
        $('#Temperature_value').html(last_element + " &#8451;");
    }else {
        $('#TDS_value').html(last_element + " ppm");
    }
}