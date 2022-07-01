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
    except paramiko.ssh_exception.AuthenticationException:
        return "认证失败",2
    except paramiko.ssh_exception.NoValidConnectionsError:
        return "不能使用ssh连接到主机%s的%s端口"%(hostname,port),2
    except TimeoutError:
        return "连接超时",2
    except paramiko.ssh_exception.SSHException:
        return "连接被服务器主动关闭",2
    else:
        stdin, stdout, stderr = client.exec_command(command)
        out_ok=stdout.read().decode('utf-8')
        out_er=stderr.read().decode('utf-8')
        time.sleep(0.001)
        client.close()
        if out_ok != '':
            return out_ok.rstrip('\n'),0
        else:
            return out_er.rstrip('\n'),1

def sftp_put():
    return