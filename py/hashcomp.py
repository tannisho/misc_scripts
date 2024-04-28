a = open('/tmp/a', 'r')
b = open('/tmp/b', 'r')
ay = {}
be = {}

for w in a:
        w = w.strip()
        ay[w] = ''

for x in b:
        x = x.strip()
        be[x] = ''

for k in ay.keys():
        if k in be:
                print k, ay[k]
