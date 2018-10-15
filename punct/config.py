import getpass

def Conf(inp):
	if inp == 'file':
		e = 'main'
	elif inp == 'path':
		e = '/home/'+getpass.getuser()+'/lists/'
	elif inp == 'tabsize':
		e = 8
	else:
		raise SystemExit
	return e