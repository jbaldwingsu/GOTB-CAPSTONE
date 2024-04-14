// server.js
const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const server = http.createServer((req, res) => {
    // Determine the requested file path
    const filePath = req.url === '/' ? 'siemdisplay.html' : req.url.slice(1); // Remove leading '/'
    const contentType = getContentType(filePath);

    // Check if the request is for the script execution endpoint
    if (req.url === '/run_python_script' && req.method === 'GET') {
        executePythonScript(res);
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
function executePythonScript(res) {
    const pythonProcess = spawn('python', ['heatmapcapture.py']);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
        res.writeHead(500);
        res.end('Error executing Python script');
    });

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        if (code === 0) {
            res.writeHead(200);
            res.end('Python script executed successfully');
        } else {
            res.writeHead(500);
            res.end('Error executing Python script');
        }
    });
}