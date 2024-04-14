// heatmapfunction.js

function createHeatmap(data) {
    const heatmapContainer = document.getElementById('heatmap');

    // Generate HTML for the heatmap
    const heatmapHTML = `
        <table>
            <tr>
                <th>Time</th>
                <th>Bandwidth Usage</th>
                <th>Number of Connections</th>
            </tr>
            <tr>
                <td>${data.time}</td>
                <td>${data.bandwidthUsage}</td>
                <td>${data.numConnections}</td>
            </tr>
        </table>
    `;

    // Insert heatmap HTML into the container
    heatmapContainer.innerHTML = heatmapHTML;
}