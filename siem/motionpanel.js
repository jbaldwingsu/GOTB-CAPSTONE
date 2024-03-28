function fetchProtocolsFromDb() {
    // AJAX request to server side script (Flask route)
    // replace 'fetch-protocols' with url of server-side script

    fetch('/fetch-protocols')
    .then(response => response.json())
    .then(data => {
    
            // process the response data (list of protocols)
            // ex assume data is array contianing protocols
            const protocols = data.protocols

            // call function to populate motion panel with fetched data
            populateMotionPanel(protocols);
    
    })
    .catch(error => {
        console.error('Error fetching protocpls:',  error);
    });
}

// function to populate motion panel with protools
function populateMotionPanel(protocols) {
    // get protocol list from element inside marquee
    const protocols = ["HTTP", "FTP", "SSH", "SMTP", "DNS", "TLS", "UDP", "TCP"];

    const protocolList = document.getElementById('protocol-list');

    // clear any existing content
    protocolList.innerHTML = '';

    // populate the protocol list with fetch protocols
    protocols.forEach(protocol => {
       protocolList.innerHTML += protocol + ' | '; // customize format as needed 
    });
}

    populateMotionPanel();

// periodically update the protocol list

function updateProtocolList() {
    // fetch protocols from the database
    fetchProtocolsFromDb();

    // set up a timer to update the protocol list at regular intervals
    setInterval(fetchProtocolsFromDb, 5000); // every 5 seconds

}

// call function to start updating
updateProtocolList();