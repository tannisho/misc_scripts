#!/usr/bin/python
import os
import pwd
import subprocess
hdl = '/tmp/hdlist.txt'
hdh = {}
pwh = {}
ws = ' '

with open(hdl, 'r') as ff:
        for i in ff:
                i = i.strip()
                u,p = i.split(':')
                pwn  = (u)
                pn   = pwd.getpwnam(pwn)
                pwn  = pn.pw_name
                pwhd = pn.pw_dir
                hdh[pwn] = pwhd
                pwh[pwhd] = p
ff.close()

for j in hdh:
        if not os.path.isdir(hdh[j]):
                print('Directory for'+ws+j+ws+'does not exist, creating..')
                subprocess.call(['mkhomedir_helper', j])
                print('Done.')


for l in pwh:
        f = open(l+'/.spacexnet_pw', 'w')
        f.write(pwh[l])
        f.close()

os.remove(hdl)
