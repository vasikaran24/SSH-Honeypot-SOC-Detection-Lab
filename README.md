# SSH-Honeypot-SOC-Detection-Lab


## Overview

This project is a custom SSH honeypot built using Python to detect brute-force attacks, capture attacker behavior, and simulate SOC monitoring workflows. The honeypot emulates an SSH service, logs attacker credentials and commands, and applies detection rules to identify malicious activity.

## Features

• Fake SSH service simulation  
• Credential harvesting detection  
• Brute force detection  
• Suspicious command detection  
• MITRE ATT&CK mapping  
• Threat scoring system  
• Session logging  
• JSON logging for SIEM integration  
• Multi-threaded attacker handling  

## Technologies Used

Python  
Socket Programming  
Cyber Security Detection Engineering  
MITRE ATT&CK Framework  
Log Analysis  

## Project Architecture

Attacker → SSH Honeypot → Detection Engine → Logging System → SOC Analysis

## Detection Logic

The system detects:

• Multiple login attempts  
• Malware download attempts  
• Privilege modification attempts  
• Command execution activity  

## MITRE ATT&CK Techniques Simulated

T1059 – Command Execution  
T1105 – Ingress Tool Transfer  
T1222 – File Permission Modification  
T1041 – Exfiltration  

##  setup and Testing


<img width="1258" height="248" alt="image" src="https://github.com/user-attachments/assets/15fbbfa0-8ab3-40ac-9b05-09a3b00e521d" />



<img width="1264" height="371" alt="image" src="https://github.com/user-attachments/assets/c5230b1f-7b9f-41a5-86cf-2f5f372d7c61" />



<img width="1363" height="426" alt="image" src="https://github.com/user-attachments/assets/bb4f255b-60f0-41a1-96ff-e9ec6ca555d2" />


<img width="1302" height="330" alt="image" src="https://github.com/user-attachments/assets/df8a43d3-8cd8-49f0-8a0e-4432a22c3961" />



<img width="1364" height="238" alt="image" src="https://github.com/user-attachments/assets/ee5d67ca-5de6-4098-87a2-4ac6c82f0829" />




Simulate attacker:

nc localhost 2222

OR

telnet localhost 2222

## Logs Generated

attacks.log → Human readable logs

sessions/ → Attacker session recordings

## output

attacks.log

10.0.2.15 command:ls MITRE:T1059 Command Execution
10.0.2.15 command:cat file1.txt MITRE:T1059 Command Execution
10.0.2.15 command:./script.sh MITRE:T1059 Command Execution
10.0.2.15 command:ls MITRE:T1059 Command Execution
10.0.2.15 command:cat file1.txt MITRE:T1059 Command Execution
10.0.2.15 command:nano file1 .txt MITRE:T1059 Command Execution
10.0.2.15 command:sudo ./script.sh MITRE:T1059 Command Execution
10.0.2.15 command:mkdir images MITRE:T1059 Command Execution
10.0.2.15 command:exit MITRE:T1059 Command Execution
10.0.2.15 command:LS MITRE:T1059 Command Execution

attacks.json

{"time": "2026-03-29 02:47:41.262996", "ip": "10.0.2.15", "username": "192.168.12.24", "password": "kgJHKHU987y769%$$%^$^", "attempts": 1, "commands": ["ls", "cat file1.txt", "nano file1 .txt", "sudo ./script.sh", "mkdir images", "exit"], "threat_score": 2}
{"time": "2026-03-29 02:52:38.315076", "ip": "10.0.2.15", "username": "192.168.12.15", "password": "qwec,bdh1233343", "attempts": 3, "commands": ["la", "ls", "sudo cat file1.txt", "sudo ./script.sh", "cat file2.log", "exit"], "threat_score": 2}
{"time": "2026-03-29 03:02:09.562458", "ip": "10.0.2.15", "username": "192.12.18.24", "password": "qweekhgh8t782", "attempts": 4, "commands": ["ls", "cat", "sudo", "mkdir fike3.txt"], "threat_score": 0}
{"time": "2026-03-29 03:08:15.217487", "ip": "10.0.2.15", "username": "john", "password": "1234john@gmail.com", "attempts": 5, "commands": ["ls", "cat file 1.txt", "cat file2.log", "sudo ./ script.sh", "exit"], "threat_score": 2}
                                                                                                     

## Learning Outcomes

This project demonstrates:

Detection engineering  
Threat monitoring  
Security logging  
Attacker behavior analysis  



## Disclaimer

This project is developed for educational and defensive security purposes only. It should be deployed in isolated lab environments and not exposed to production systems.
