import collections
list = '/tmp/1'
seen = set()
uniq = []

a = open(list, 'r')

for w in a:
        w = w.strip()
        if w not in seen:
                uniq.append(w)
                seen.add(w)

for j in uniq:
        print(j)
