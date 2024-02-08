-- SQLite schema
CREATE TABLE network_logs (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    source_ip TEXT,
    destination_ip TEXT,
    protocol TEXT,
    message TEXT
);

-- sample data
INSERT INTO network_logs (timestamp, source_ip, destination_ip, protocol, message)
VALUES ('2024-02-06 12:00:00', '192.168.1.100', '8.8.8.8', 'TCP', 'Sample TCP traffic from source to destination.'),
       ('2024-02-06 12:01:00', '192.168.1.101', '8.8.4.4', 'UDP', 'Sample UDP traffic from source to destination.');
       ('2024-02-06 12:02:00', '192.168.1.102', '8.8.5.5', 'TCP', 'Sample TCP traffic from source to destination.');

