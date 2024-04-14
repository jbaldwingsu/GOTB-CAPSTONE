function fetchAndDisplayLogs() {
    fetch('network_log.txt')
        .then(response => response.text())
        .then(data => {
            const logsTableBody = document.getElementById('logs-body'); // Select table body for logs

            // Split log entries by newline character
            const logEntries = data.trim().split('\n');

            // Iterate over each log entry and create table rows
            logEntries.forEach(entry => {
                // Split entry by comma and space
                const [timestamp, source_ip, destination_ip, protocol] = entry.split(/ - |, /);

                // Create table row and insert cells with extracted values
                const logRow = document.createElement('tr');
                logRow.classList.add('log-entry');

                // Add classes for protocol type
                logRow.innerHTML = `
                    <td class="log-timestamp ${timestamp}">${timestamp}</td>
                    <td class="log-source ${source_ip}">${source_ip}</td>
                    <td class="log-destination ${destination_ip}">${destination_ip}</td>
                    <td class="log-protocol ${protocol}">${protocol}</td>
                `;

                // Append row to table body
                logsTableBody.appendChild(logRow);
            });

            // Analyze log entries
            const protocolCounts = analyzeLogs(logEntries);

            console.log('Protocol counts:', protocolCounts);
            // Update the pie chart
            updatePieChart(protocolCounts);
        })
        .catch(error => console.error('Error fetching logs:', error));
}

// Call fetchAndDisplayLogs() function to fetch logs and update the table and pie chart
fetchAndDisplayLogs();