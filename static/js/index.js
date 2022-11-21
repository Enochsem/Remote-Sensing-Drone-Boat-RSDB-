
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

    // sidebar
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

    // floating button to toggle sidebar
    $('#floating_button').on('click', function () {
        // console.log("clicked")
        $('#sidebar').toggleClass('active');
    });

    // notification Tables
    $('#notification_table').DataTable( {
        dom: 'Bfrtip',
        buttons: [ {extend: 'excelHtml5', title: notification_Title},{extend: 'pdfHtml5',title: notification_Title}]
    } );

     // Ph_Sensor Tables
     $('#Ph_Sensor').DataTable( {
        dom: 'Bfrtip',
        buttons: [{extend: 'excelHtml5', title: Ph_Sensor_Title}, {extend: 'pdfHtml5',title: Ph_Sensor_Title}]
    } );

    // tds_sensor
    $('#tds_sensor').DataTable( {
        dom: 'Bfrtip',
        buttons: [ {extend: 'excelHtml5', title: TDS_Title}, { extend: 'pdfHtml5',title: TDS_Title}]
    } );

    // turbidity_sensor
    $('#turbidity_sensor').DataTable( {
        dom: 'Bfrtip',
        buttons: [{extend: 'excelHtml5', title: Turbidity_Title}, {extend: 'pdfHtml5',title: Turbidity_Title}]
    } );

    // temperature_sensor
    $('#temperature_sensor').DataTable( {
        dom: 'Bfrtip',
        buttons: [{extend: 'excelHtml5',title: Temperature_Title},{extend: 'pdfHtml5',title: Temperature_Title}]
    } );


    // Graphs Fuction cals
    phLineGraph()
    temperatureGraph()
    tubidityGraph()
    tdsGraph()
    

    // single fuction to raw all graphs
    // temperal_co=[{x:'green dgsgshshsghjs',y:54},{x:'blue dgsgshshsghjs',y:64}]
    // let temperal_line_graph = null
    // drawGraph("line","temperal G",temperal_co,"temperal",temperal_line_graph,"rgba(255,0,0,0.3)","rgba(0,0,255,0.5)")

});



function drawGraph(graphType,graphTitle,coordinate,htmlIdTagSelector, renderGraphObject, borderColor=null, backgroundColor=null){
    const data = {
        datasets: [{label: graphTitle ,fill: false,lineTension: 0,
        backgroundColor: backgroundColor,
        borderColor: borderColor,
        data: coordinate}]
    }

    const config = {
        type: graphType,
        data: data,
        options: {
            scales: {
                x: {
                    ticks: {
                        callback: function(value, index) {
                            // console.log(this.getLabelForValue(value))
                            let short_date = this.getLabelForValue(value).slice(5,7)+ "|"+this.getLabelForValue(value).slice(8,10)+"|"+this.getLabelForValue(value).slice(17)
                            return `${short_date}`
                          }
                    }
                }
            }
        }
    }
    if(renderGraphObject != null){renderGraphObject.destroy();}
    // rendering the chart
    renderGraphObject = new Chart(document.getElementById(htmlIdTagSelector),config);
}





let ph_line = null;
let temperature_line = null; 
let tubidity_bar = null;
let tds_bar = null;

var ph_coordinate =[];
// Ph graph
function phLineGraph(){
    // 
    const data = {
        datasets: [{label: 'Ph Sensor',fill: false,lineTension: 0,
        backgroundColor: "rgba(250, 174, 27,3.1)",
        borderColor: "rgba(8, 152, 231,3.0)",
        data: ph_coordinate}]
    }

    const config = {
        type: "line",
        data: data,
        options: {
            scales: {
                x: {
                    ticks: {
                        // Include a dollar sign in the ticks
                        callback: function(value, index) {
                            // console.log(this.getLabelForValue(value))
                            // console.log(this.getLabelForValue(index))xxx
                            let short_date = this.getLabelForValue(value).slice(5,7)+ "|"+this.getLabelForValue(value).slice(8,10)+"|"+this.getLabelForValue(value).slice(17)
                            return `${short_date}`
                          }
                    }
                }
            }
        }
    }
    if(ph_line != null){ph_line.destroy();}
    // rendering the chart
     ph_line = new Chart(document.getElementById('ph'),config);
}

// temperature line graph
var temperature_coordinate = [];
function temperatureGraph(){

    data = {
        datasets: [{label: 'Temperature',fill: false,lineTension: 0,
        backgroundColor: "rgba(250, 174, 27,3.1)",
        borderColor: "rgba(8, 152, 231,3.0)",
        data:temperature_coordinate}]
    },

    config =  {
        type: "line",
        data: data,
        options: {
            legend: {display: false},
            scales: {
                x: {
                    ticks: {
                        callback: function(value, index) {
                            let short_date = this.getLabelForValue(value).slice(8,10)
                            return `${3}`+`${short_date}`
                          }
                    }
                }
            }
         }
        }

    if(temperature_line != null){temperature_line.destroy();}
    temperature_line = new Chart($("#temperature"), config);
}

// tubidity bar graph
tubidity_coordinate = [];
function tubidityGraph(){
    const ctx = document.getElementById('turbidity');
    if(tubidity_bar!=null){tubidity_bar.destroy();} //prevent destroy error

    data =  {
        datasets: [{
            label: 'Turbidity',
            data: tubidity_coordinate,
            backgroundColor: ["rgba(250, 174, 27,5.1)",'rgb(255, 99, 132)','rgb(255, 99, 2)'],
            borderColor: ["rgba(50, 17, 207,0.1)",'rgba(255, 99, 132, 1)'],
            borderWidth: 1}]
    }

    config = {
        type: 'bar',
        data: data,
        options: {
            scales: { y: { beginAtZero: true} },
            scales: {
                x: {
                    ticks: {
                        callback: function(value, index) {
                            return `${value}`
                          }
                    }
                }
            }
          }
    }
    tubidity_bar =  new Chart(ctx, config);
}

// tds bar chart
tds_coordinate = [];
function tdsGraph(){
    const tag = document.getElementById('tds');

    const data = {
        datasets: [{
          label: 'TDS Sensor',
          data: tds_coordinate,
          backgroundColor: ["rgba(250, 174, 27,5.1)",'rgb(255, 99, 132)','rgb(255, 99, 2)'],
          hoverOffset: 4
        }]
      };

    var config = {type: 'bar', data: data}

    if(tds_bar!=null){tds_bar.destroy(); } //prevent destroy errorpi
    tds_bar = new Chart(tag, config);
}



// update charts on dashboard
function updateGraphData(chart, data) {
    // chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

// custom date
function getdate () {
    const pad = (n,s=2) => (`${new Array(s).fill(0)}${n}`).slice(-s);
    const d = new Date();
    return `${pad(d.getFullYear(),4)}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
}

//Device_id got from hidden input field on dashboard
function plot_graph(sensor_type, chart, coordinates){
    device_id = $("#device_id").val(); 
    // console.log(device_id);
    $.ajax({
        type: 'GET',
        url: '/get_graph_data',
        data: {'device_id': device_id, 'sensor_type': sensor_type },
        success: (data) => {
          graph_data =  data['response'];
            // wiil change data return type to list of maps (json object)
          for (let index = 0; index < graph_data.length; index++) {
            coordinates.push({x:`${graph_data[index]["date"]}`, y:graph_data[index]["value"]});//, {x:'green',y:54}
            // String(graph_data[index]["date"]).substring(0,11)
          }
  
          updateGraphData(chart, coordinates);
          // graph_data.forEach(element => {
          //     coordinates.push({x:element[3], y:graph_date})
          // });
          
          //for dashboard cards
          var last_element = graph_data[graph_data.length-1]['value'];
          set_card_data(sensor_type, last_element);

        },
  
    });
}

// set card data on dashboard
function set_card_data(sensor_type,last_element){
    if (sensor_type == "Ph") {
        $('#Ph_value').html(last_element);
        // console.log('hereyyyy' + last_element);
    }else if(sensor_type == "Turbidity"){
        $('#Turbidity_value').html(last_element + " NTU");
    }else if(sensor_type == "Temperature"){
        $('#Temperature_value').html(last_element + " &#8451;");
    }else {
        $('#TDS_value').html(last_element + " ppm");
    }
}

// update charts on custom Data Page
function updateComboGraph(chart, ph_sensor,temp_sensor,tur_sensor,tds_sensor) {
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(ph_sensor);
        dataset.data.push(temp_sensor);
        dataset.data.push(tur_sensor);
        dataset.data.push(tds_sensor);
    });
    chart.update();
}




/////////////========= combo_graph =========/////////////
let combo_graph = null;
var ph_sensor = [];
var tds_sensor = [];
var temp_sensor = [];
var tur_sensor = [];

// comboLineGraph
$(document).ready(function(){
    const data = {
        datasets: [
            {
            type: "line",
            label: 'Ph',fill: false,lineTension: 0,
            backgroundColor: "rgba(0,0,205,1.0)",
            borderColor: "rgba(0,0,205,0.1)",
            data: ph_sensor
            },
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
                backgroundColor: "rgba(222,222,0,1.0)"
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


// load data from api on ajax call (not been used now)
const baseURL = "http://127.0.0.1:5001"


// fetch combo graph data
$(document).ready(function(){
    // console.log(baseURL+"hehe");
    device_id = $("#device_id").val();
    // console.log("checkinh... "+device_id)
    $.ajax({
      type: 'GET',
      url: '/all_graph_data',
      data: {'device_id': device_id},
      success: (data) => {
        // console.log("checking " + data['response']);
        var graph_data =  data['response'];
        // wiil change data return type to list of maps (json object)
        for (let index = 0; index < graph_data.length; index++) {
            if (graph_data[index]['sensor']=="Ph") {
                ph_sensor.push({x:graph_data[index]["date"], y:graph_data[index]["value"]});
            }else if(graph_data[index]["sensor"]=="Temperature"){
                temp_sensor.push({x:graph_data[index]["date"], y:graph_data[index]["value"]});
            }else if(graph_data[index]["sensor"]=="Turbidity"){
                tur_sensor.push({x:graph_data[index]["date"], y:graph_data[index]["value"]});
            }else if(graph_data[index]["sensor"]=="TDS"){
                tds_sensor.push({x:graph_data[index]["date"], y:graph_data[index]["value"]});
            }
        }
        // graph_data.forEach(element => {
        //     yaxis.push({x: graph_date, y: element[3]}, {x: element[3], y: 10});
        // });

        updateComboGraph(combo_graph, ph_sensor,temp_sensor,tur_sensor,tds_sensor)

      },

    });

});




$(document).ready(function(){
    plot_graph("Ph",ph_line,ph_coordinate); //Ph Graph
    plot_graph(sensor_type="Temperature", chart=temperature_line, coordinates=temperature_coordinate); //temperature Graph
    plot_graph(sensor_type="Turbidity", chart=tubidity_bar, coordinates=tubidity_coordinate); //Turbidity Graph
    plot_graph(sensor_type="TDS", chart=tds_bar, coordinates=tds_coordinate); //TDS Graph

    // combo graph

});




setInterval(() => {}, 5000);  
// 5 sec

// Shijou Saikyou no Daimaou, Murabito A ni Tensei suru Episode 9 
//     // from flask_cors import CORS