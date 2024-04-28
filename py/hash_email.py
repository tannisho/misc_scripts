import re
import sys
ld = '/tmp/list1'
emh ={}

with open(ld, 'r') as ff:
	i = ff.read()
	a = i.split('\n\n')
ff.close()

for b in a:
	matchobj0 = re.search("^(# refldap:|\\.)", b)
	if not matchobj0:
		c,d = b.split('sAMAccountName:')
		e,f = d.split('mail:')
		e = e.strip()
		e = e.lower()
		f = f.strip()
		emh[e] = f

for g in emh:
	print(emh[g]+':'+g+':')
