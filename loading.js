// Function to show the loading spinner / handle loading for Port Scanner Function
function showLoadingSpinner() {
    document.getElementById('loading-spinner').style.display = 'block';
}

// Function to hide the loading spinner
function hideLoadingSpinner() {
    document.getElementById('loading-spinner').style.display = 'none';
}

// Get the port scan button element
const portScanBtn = document.getElementById('port-scan-btn');

// Add event listener to the port scan button
portScanBtn.addEventListener('click', function() {
    // Show the loading spinner when the button is clicked
    showLoadingSpinner();

    // Simulate port scanning process (replace this with your actual port scanning logic)
    setTimeout(function() {
        // Once port scanning is complete, hide the loading spinner
        hideLoadingSpinner();

        // Display the port scanning results
        // (You would typically update the UI with the results here)
        document.getElementById('port-scan-results').innerText = "Open ports: 80, 443";
    }, 3000); // Simulating a 3-second delay for demonstration
});
