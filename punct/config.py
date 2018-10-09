import getpass

def Conf(inp):
	if inp == 'file':
		e = 'main'
	elif inp == 'path':
		e = '/home/'+getpass.getuser()+'/lists/'
	else:
		raise SystemExit
	return e