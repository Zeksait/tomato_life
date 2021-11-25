/* globals Chart:false, feather:false */

(function () {
    'use strict'

    feather.replace({'aria-hidden': 'true'})

    // Graphs
    var ctx = document.getElementById('myChart')
    // eslint-disable-next-line no-unused-vars
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            datasets:
            [
            {data: JSON.parse({{ data_str }}),
             lineTension: 0,
             backgroundColor: 'transparent',
             borderColor: '#007bff',
             borderWidth: 4,
             pointBackgroundColor: '#007bff'},

             {data: [1, 2, 3, 4, 2, 5, 7],
             lineTension: 0,
             backgroundColor: 'transparent',
             borderColor: '#ff0000',
             borderWidth: 4,
             pointBackgroundColor: '#800000'
             }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: false
                    }
                }]
            },
            legend: {
                display: true
            }
        }
    })
})()
