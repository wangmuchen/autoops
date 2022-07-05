#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import setget_tab
import libssh

command = "LANG=en_US.UTF-8 virsh list --all"

host_list = setget_tab.get_host_info()
for i in range(len(host_list)):
    msg = libssh.ssh_exec(command,host_list[i])
    if msg[1] == 0:
        print("主机%s的虚拟机清单"%host_list[i][0])
        print(msg[0])
