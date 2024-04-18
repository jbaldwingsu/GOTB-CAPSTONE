// Function to fetch and display port scanning results
function performPortScan() {
    const targetHost = document.getElementById('target-host').value;
    const targetPorts = document.getElementById('target-ports').value;

    fetch('/run_port_scan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ targetHost, targetPorts }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to execute port scanning script');
        }
        return response.text();
    })
    .then(data => {
        // Display port scanning results in the HTML container
        document.getElementById('port-scan-results').innerHTML = `<pre>${data}</pre>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Event listener for the port scan button
document.getElementById('port-scan-btn').addEventListener('click', performPortScan);
