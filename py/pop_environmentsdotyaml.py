a = open('nodes', 'r')
env = 'oldpe_production'
ws  = ':    '

for i in a:
	i = i.strip()
	print("'"+i+"'"+ws+"'"+env+"'")
