# GOTB-CAPSTONE
This is our Guardians Of The Binary - System Information & Event Management (SIEM) system.
Our SIEM allows the user to have a live visualization of the series of packetcaptures, network traffic activity,
and more -- giving users the ability to have a clear view of some of the a activity that goes on within
a network that most would not be aware to.

## Project Dependencies:
```python
pip install scapy
pip install python-dotenv
```

## To Run Program
** Simple to run
While in the 'GOTB-CAPSTONE' directory simply run:
    'node server.js' in your command prompt to launch the localhost:3000 server and operate the GOTB-SIEM
    Using control/cmd + click the http://localhost:3000/ link you will be take to our main page



## In order for email alerts to function:

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

# Testing
To test program we have included a 'test_packetcapture.py' script that takes a test of the interaction
of some supporting JavaScript files that are used to parse data captured to its own .txt file that is
later used to display the results on our localhost page.

# To Run Test 
    Simply remain in the 'GOTB-CAPSTONE' directory and run 'pytest'to run the tests of our programs functionality