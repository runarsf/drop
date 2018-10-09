
def Conf(inp):
	if inp == 'file':
		e = 'main'
	elif inp == 'path':
		e = '/lists/'
	else:
		raise SystemExit
	return e