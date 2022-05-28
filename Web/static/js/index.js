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
var clientTitle = "Ph Sensor "+date;

var agentTitle = "Turbidity Sensor "+date;
var monitortTitle = "TDS Sensor "+date;
var manageClient = 'Temperature Sensor '+date;





$(document).ready(function () {
    // agentTables
    $('#susuAgent').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                title: agentTitle
            },
            {
                extend: 'pdfHtml5',
                title: agentTitle
            }
        ]
    } );
});


$(document).ready(function () {
    // monitor
    $('#monitor').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            {
                extend: 'excelHtml5',
                title: monitortTitle
            },
            {
                extend: 'pdfHtml5',
                title: monitortTitle
            }
        ]
    } );
});





// Ph graph
$(document).ready(function(){
    var xValues = [50,60,70,80,90,100,110,120,130,140,150];
    var yValues = [7,8,8,9,9,9,10,11,14,14,15];
    
    new Chart("ph", {
        type: "line",
        data: {labels: xValues,
                datasets: [{label: 'Ph',fill: false,lineTension: 0,
                        backgroundColor: "rgba(0,0,255,1.0)",
                        borderColor: "rgba(0,0,255,0.1)",
                        data: yValues}]
            },
        options: {legend: {display: false},scales: {yAxes: [{ticks: {min: 6, max:16}}],} }
        });
});



$(document).ready(function(){
var xValues = [50,60,70,80,90,100,110,120,130,140,150];
var yValues = [7,8,8,9,9,9,10,11,14,14,15];

new Chart("myChart", {
    type: "line",
    data: {labels: xValues,
            datasets: [{label: 'Temperature',fill: false,lineTension: 0,
                    backgroundColor: "rgba(0,0,255,1.0)",
                    borderColor: "rgba(0,0,255,0.1)",
                    data: yValues}]
        },
    options: {legend: {display: false},scales: {yAxes: [{ticks: {min: 6, max:16}}],} }
    });
});






// bar graph
$(document).ready(function(){
    const ctx = document.getElementById('tubidity');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: 'Turbidity',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
});






// pie chart
$(document).ready(function(){
    const tag = document.getElementById('tds');

    
    const data = {
        labels: [
          'Red',
          'Blue',
          'Yellow'
        ],
        datasets: [{
          label: 'TDS Sensor',
          data: [300, 50, 100],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)'
          ],
          hoverOffset: 4
        }]
      };

    const myChart = new Chart(tag,{
        type: 'pie',
        data: data,
    });

});