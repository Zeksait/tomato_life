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
            [{data: [1, 15, 3, 14, 25, 59, 17, 21, 14, 8],
             lineTension: 0,
             backgroundColor: 'transparent',
             borderColor: '#ff0000',
             borderWidth: 4,
             pointBackgroundColor: '#800000'
             },
                {data: [12, 17, 15, 20, 24, 26, 27, 34, 19, 18],
             lineTension: 0,
             backgroundColor: 'transparent',
             borderColor: '#121212',
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
