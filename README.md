# GOTB-CAPSTONE

## Project Dependencies:
```python
pip install scapy
```

In order for email alerts to function:

1. go to myaccount.google.com/apppasswords and generate a password code to be used with python API's
2. in the terminal, install dotenv module:
    ```python
    pip install python-dotenv
    ```
3. in the same directory as "packetcapture.py", create a .env file with the following:
    ``` 
    API_KEY="the pass code generated in step 1"
    SENDER="your email"
    RECIPIENT="recipient email"
    ```
After completing these steps, you will recieve alert emails if a packet contains a critical security risk, as well as a summary after every packet capture.

Example: https://imgur.com/a/epIKZuR

Terminal output:
```
Packet capture has started ... (Ctrl+C to stop)
GOTB SIEM Alert email sent to wb02450@georgiasouthern.edu
GOTB SIEM Alert email sent to wb02450@georgiasouthern.edu
Packet capture has stopped.
GOTB SIEM Summary Report email sent to wb02450@georgiasouthern.edu
```