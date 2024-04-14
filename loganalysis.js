/* Used to capture protocol traffic and make analysis into pie chart display*/

// function to capture counts of protocols in packetcapture.py
function analyzeLogs(logs) {
    let protocolCounts = {
        ICMP: 0,
        TCP: 0,
        UDP: 0,
        Other: 0
    };

    // loop through logs and count occurrences of each protocol
    logs.forEach(log => {
        // Split log entry by comma and space
        const logParts = log.split(', ');

        // Extract the protocol from the logParts
        const protocol = logParts[3]?.trim();

        /* test to ensure protocol counting is accurate */
        // console.log('Parsed log entry:', logParts);
        // console.log('Extracted protocol:', protocol);

        switch (protocol) {
            case 'ICMP':
                protocolCounts.ICMP++;
                break;

            case 'TCP':
                protocolCounts.TCP++;
                break;

            case 'UDP':
                protocolCounts.UDP++;
                break;

            default:
                protocolCounts.Other++;
        }
    });
    return protocolCounts;
}

// function to update pie chart with the protocol trend data
function updatePieChart(protocolCounts) {
    const ctx = document.getElementById('protocolChart').getContext('2d');

    // create data for chart
    const data = {
        labels: Object.keys(protocolCounts),
        datasets: [{
            label: 'Protocol Trend Count',
            data: Object.values(protocolCounts), // Calculate percentage for each protocol count
            backgroundColor: [
                'rgba(255, 99, 132, 0.7)', // Red for ICMP
                'rgba(54, 162, 235, 0.7)', // Blue for TCP
                'rgba(255, 206, 86, 0.7)', // Yellow for UDP
                'rgba(75, 192, 192, 0.7)' // Green for Other
            ],
            borderWidth: 1
        }]
    };

    // create options for the chart
    const options = {
        responsive: true,
        maintainAspectRatio: false,
        tooltips: {
            callbacks: {
                label: function (tooltipItem, data) {
                    const protocolCount = data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
                    const totalProtocols = data.datasets[tooltipItem.datasetIndex].data.reduce((total, count) => total + count, 0);
                    const protocolPercentage = ((protocolCount / totalProtocols) * 100).toFixed(2) + '%'; // Calculate percentage
                    return data.labels[tooltipItem.index] + ': ' + protocolCount + ' (' + protocolPercentage + ')';
                }
            }
        }
    };

    // create and update pie chart
    const pieChart = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: options
    });
}