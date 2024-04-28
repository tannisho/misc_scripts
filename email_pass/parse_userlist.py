# meant to generate colon delimited list for adduser.py run on ipa server

import re
import pwd
import subprocess

pass_m = 'pw/password_map_last'
xd = subprocess.check_output(['eyaml', 'decrypt', '-f', pass_m]).splitlines()

for i in xd:
	i = i.strip()
	match = re.search('^(---|\\.)', i)
        if not match:
		receiver_email,user_name,password_clear = i.split(':')
        	pw = pwd.getpwnam(user_name)
                pwn = pw.pw_name
                pwfn = pw.pw_gecos
                pwfn = re.sub(' [A-Z]* ', ' ', pwfn)
		firstname,lastname = pwfn.split()
                print(password_clear+':'+pwn+':'+firstname+':'+lastname)
