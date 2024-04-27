#!/data/data/com.termux/files/usr/bin/python

import paramiko
import socket
import sys

def test_proxy(proxy):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((proxy.split(':')[0], int(proxy.split(':')[1])))
        s.close()
        return True
    except:
        return False

def test_payload(payload):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(payload.split(':')[0], username='DragonSCP', password='1234', port=int(payload.split(':')[1]))
        ssh.close()
        return True
    except:
        return False

def main():
    payloads = ['mastertechnet.online:22']

    for payload in payloads:
        if test_payload(payload):
            print(f'Payload {payload} is working.')
        else:
            print(f'Payload {payload} is not working.')

if __name__ == '__main__':
    main()
