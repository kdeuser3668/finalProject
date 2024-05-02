// script.js

// Function to make an AJAX request
function fetchData() {
    // Get the form data
    var symbol = document.getElementById('symbol').value;
    var chartType = document.getElementById('chartType').value;

    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Define the URL of your Flask endpoint
    var url = '/result';

    // Configure the request
    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    // Define the callback function when the request is complete
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            // Request was successful, handle the response here
            var response = JSON.parse(xhr.responseText);
            var dates = response.chartData.dates;
            var prices = response.chartData.prices;

            var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: dates,
                    datasets: [{
                        label: 'Stock Price',
                        data: prices,
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
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
        } else {
            // Request failed
            console.error('Request failed with status ' + xhr.status);
        }
    };

    // Encode form data as URL parameters
    var params = 'symbol=' + encodeURIComponent(symbol) + '&chartType=' + encodeURIComponent(chartType);

    // Send the request with form data
    xhr.send(params);
}

// Call the fetchData function when the page is loaded
window.onload = fetchData;
