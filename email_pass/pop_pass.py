import re, sys, random, string

ld = '/tmp/one'


with open(ld, 'r') as ff:
	for i in ff:
		i = i.strip()
		a,b,c = i.split(':')
		sample_str = ''.join((random.choice(string.ascii_letters) for i in range(7)))
    		sample_str += ''.join((random.choice(string.digits) for i in range(5)))
    		sample_list = list(sample_str)
    		random.shuffle(sample_list)
    		final_string = ''.join(sample_list)
		print(a+':'+b+':'+'DEC::PKCS7['+final_string)
ff.close()
