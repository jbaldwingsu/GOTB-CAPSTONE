// portscan.js

// Function to fetch and display port scanning results
function performPortScan() {
    fetch('/run_port_scan', { method: 'GET' })
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
