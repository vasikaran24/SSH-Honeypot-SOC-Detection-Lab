import socket
import threading
import datetime
import json
import os

HOST="0.0.0.0"
PORT=2222

if not os.path.exists("sessions"):
    os.mkdir("sessions")

login_attempts={}

def log_text(data):

    file=open("attacks.log","a")

    file.write(data+"\n")

    file.close()


def log_json(data):

    file=open("attacks.json","a")

    json.dump(data,file)

    file.write("\n")

    file.close()


def threat_score(password_attempts,commands):

    score=0

    if password_attempts>5:
        score+=5

    suspicious=[
        "wget",
        "curl",
        "chmod",
        "nc",
        "bash",
        "sh",
        "python",
        "perl"
    ]

    for cmd in commands:

        for s in suspicious:

            if s in cmd:
                score+=2

    return score


def mitre_mapping(command):

    if "wget" in command:
        return "T1105 Ingress Tool Transfer"

    if "curl" in command:
        return "T1105 File Download"

    if "chmod" in command:
        return "T1222 File Permission Modify"

    if "nc" in command:
        return "T1041 Exfiltration"

    return "T1059 Command Execution"


def client_handler(client,addr):

    ip=addr[0]

    print("Attacker:",ip)

    client.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu\r\n")

    client.send(b"login: ")

    username=client.recv(1024).decode().strip()

    client.send(b"Password: ")

    password=client.recv(1024).decode().strip()

    if ip not in login_attempts:
        login_attempts[ip]=0

    login_attempts[ip]+=1

    commands=[]

    session_file=open(f"sessions/{ip}.txt","a")

    session_file.write(f"\nSession {datetime.datetime.now()}\n")

    session_file.write(f"Username:{username}\n")

    session_file.write(f"Password:{password}\n")

    client.send(b"Welcome to Ubuntu 20.04 LTS\n")

    while True:

        client.send(b"$ ")

        command=client.recv(1024).decode().strip()

        if not command:
            break

        commands.append(command)

        session_file.write(command+"\n")

        mitre=mitre_mapping(command)

        log_text(f"{ip} command:{command} MITRE:{mitre}")

        if command=="exit":
            break

        if command=="ls":
            client.send(b"file1.txt file2.log script.sh\n")

        elif command=="whoami":
            client.send(b"root\n")

        elif command=="pwd":
            client.send(b"/root\n")

        else:
            client.send(b"Command not found\n")

    session_file.close()

    score=threat_score(login_attempts[ip],commands)

    attack_data={

        "time":str(datetime.datetime.now()),
        "ip":ip,
        "username":username,
        "password":password,
        "attempts":login_attempts[ip],
        "commands":commands,
        "threat_score":score
    }

    log_json(attack_data)

    print("Threat score:",score)

    client.close()


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen(100)

print("SOC SSH Honeypot running on port 2222")

while True:

    client,addr=server.accept()

    thread=threading.Thread(
        target=client_handler,
        args=(client,addr)
    )

    thread.start()
