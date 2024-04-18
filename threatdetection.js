// threatdetection.js

// Function to detect threats
function detectThreats() {
    fetch('/detect_threats', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    })
    .then(response => response.text())
    .then(data => {
        // Display threat detection results
        document.getElementById('threat-detection-results').innerText = data;
    })
    .catch(error => {
        console.error('Error detecting threats:', error);
    });
}

function detectThreats() {
    fetch('/detect_threats', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({})
    })
    .then(response => response.text())
    .then(data => {
        // Display threat detection results
        document.getElementById('threat-detection-results').innerText = data;
    })
    .catch(error => {
        console.error('Error detecting threats:', error);
    });
}


// Attach event listener to threat detection button
document.getElementById('threat-detect-btn').addEventListener('click', detectThreats);
