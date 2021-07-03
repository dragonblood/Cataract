// var pctx = document.getElementById('piechart').getContext('2d');
// var piechart = new Chart(pctx, {
//     type: 'radar',
//     data: {
//         labels: sentiment,
//         datasets: [{
//             data: sentiment_data,
//             backgroundColor: [
//                 'rgba(255, 206, 86, 0.2)', //yello
//                 'rgba(75, 192, 128, 0.2)', //green
//                 'rgba(255, 99, 132, 0.2)', //pink
//             ],
//             borderColor: [
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(75, 192, 128, 1)',
//                 'rgba(255, 99, 132, 1)',
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         legend: {
//             display: false,
//             position: "bottom"
//         },
//         title: {}
//     }
// });

var bctx = document.getElementById('barchart').getContext('2d');
var barchart = new Chart(bctx, {
    type: 'bar',
    data: {
        labels: lables,
        datasets: [{
            data: lables_score,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            display: false,
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});