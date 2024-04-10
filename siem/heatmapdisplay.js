// heatmapdisplay.js
function captureData() {
    // Send a request to the server to execute the Python script
    fetch('/run_python_script', { method: 'GET' }) // Specify method: 'GET'
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to execute Python script');
            }
            return response.text();  // Assuming the Python script writes data to a text file
        })
        .then(data => {
            // Parse the text file and update the heatmap display
            updateHeatmapDisplay(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });

    console.log("Data Captured");
}

function updateHeatmapDisplay(data) {
    // Parse the text data and update the heatmap display
    const capturedData = parseCapturedData(data);

    // Update the heatmap display with the captured data
    createHeatmap(capturedData);
}

function parseCapturedData(data) {
    // Parse the text data to extract time, bandwidth usage, and number of connections
    // Example: data format is "Time: 12:00, Bandwidth Usage: 123456, Num Connections: 10"
    const parts = data.split(', ');
    const time = parts[0].split(': ')[1];
    const bandwidthUsage = parseInt(parts[1].split(': ')[1]);
    const numConnections = parseInt(parts[2].split(': ')[1]);

    return { time, bandwidthUsage, numConnections };
}

// Wait for the DOM content to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Add event listener to the button when the DOM is loaded
    document.getElementById("capture-data-btn").addEventListener("click", captureData);
});
