import re
import sys
ld = '/tmp/list1'
tg = '/tmp/list2'
ldh ={}
tgh ={}

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
		ldh[f] = e

with open(tg, 'r') as gg:
	for i in gg:
		i = i.strip()
		tgh[i] = ''
gg.close()
	

for g in ldh:
	if g in tgh:
		print(g+':'+ldh[g]+':')
