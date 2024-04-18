const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const server = http.createServer((req, res) => {
    // Determine the requested file path
    const filePath = req.url === '/' ? 'siemdisplay.html' : req.url.slice(1); // Remove leading '/'
    const contentType = getContentType(filePath);

    // Check if the request is for the port scan endpoint
    if (req.url === '/run_port_scan' && req.method === 'POST') {
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString(); // Convert Buffer to string
        });
        req.on('end', () => {
            const { targetHost, targetPorts } = JSON.parse(body);
            executePortScan(res, targetHost, targetPorts);
        });
    } else if (req.url === '/detect_threats' && req.method === 'POST') {
        // Handle the threat detection endpoint
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString(); // Convert Buffer to string
        });
        req.on('end', () => {
            // Placeholder for threat detection logic
            const threatDetectionResults = "Placeholder: Threats detected!";
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end(threatDetectionResults);
        });
    } else {
        // Read the requested file
        fs.readFile(filePath, (err, data) => {
            if (err) {
                if (err.code === 'ENOENT') {
                    // File not found
                    res.writeHead(404);
                    res.end('File Not Found');
                } else {
                    // Other error
                    res.writeHead(500);
                    res.end(`Server Error: ${err.message}`);
                    console.error('Server Error:', err);
                }
            } else {
                // File found, serve it with appropriate content type
                res.writeHead(200, { 'Content-Type': contentType });
                res.write(data);
                res.end();
            }
        });
    }
});

server.listen(3000, 'localhost', () => {
    console.log('Server is running at http://localhost:3000/');
});

// Function to determine content type based on file extension
function getContentType(filePath) {
    const extname = path.extname(filePath);
    switch (extname) {
        case '.html':
            return 'text/html';
        case '.css':
            return 'text/css';
        case '.js':
            return 'text/javascript';
        case '.txt':
            return 'text/plain';
        default:
            return 'application/octet-stream';
    }
}

// Function to execute the Python script
function executePortScan(res, targetHost, targetPorts) {
    const pythonProcess = spawn('python', ['portscanner.py', targetHost, targetPorts]);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
        // Send the port scanning results to the client
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end(data);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
        res.writeHead(500);
        res.end('Error executing port scanning script');
    });

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });
}
