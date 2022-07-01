#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import paramiko

def ssh_exec(command,host_list=[]):
    hostname = host_list[0]
    port = host_list[1]
    username = host_list[2]
    password = host_list[3]
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname,port,username,password)
    except paramiko.ssh_exception.SSHException:
        return "目标主机断开会话",2
    stdin, stdout, stderr = client.exec_command(command)
    out = stdout.read().decode('utf-8')
    err = stderr.read().decode('utf-8')
    time.sleep(0.001)
    client.close()
    if out != '':
        return out.strip('\n'),0
    elif err != '':
        return err.strip('\n'),1
def sftp_put():
    return