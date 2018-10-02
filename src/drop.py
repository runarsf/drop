""" main """
import os
import sys

def verify():
    try:
        import config as c
    except:
        if not os.path.isfile('config.py'):
            confile = open('config.py', 'w+')

            confile.write('filename = \'main\'\n')
            confile.write('filepath = \'./lists/\'')

            confile.close()
            print('created config from template')
    finally:
        import config as c
        if not os.path.exists(c.filepath):
        	try:
        		print("Creating file directory")
        		os.makedirs(c.filepath)
        	except:
        		print("Could not create directory. Check config formatting.\nExiting...")
        		raise SystemExit
        if not os.path.isfile(c.filepath+c.filename):
        	try:
        		print("Creating file")
        		file = open(c.filepath+c.filename, 'w+')
        		file.close()
        	except:
        		print("Could not create file. Check config formatting.\nExiting...")
        		raise SystemExit
verify()

def helpme():
    print('\n\tUsage: python3 drop.py [arguments]\n')
    print('\t       -h          Shows this dialog.')
    print('\t       -c          Check/uncheck list.')
    print('\t       -l List     Sets which todo list to use.')
    print('\t                   Creates it if not existing.')
    print('\t       -a Content  Adds an entry to your todo list.')
    print('\t       -r Index    Removes entry from your todo list.')
    print('')

def add():
    pass

def remove():
    pass

def setList():
    pass

def check():
    pass

if len(sys.argv) > 3:
    print('Too many arguments!')
    raise SystemExit
elif len(sys.argv) <= 1:
    print('Too few arguments!')
    raise SystemExit

if '-h' in sys.argv:
    helpme()
elif '-a' in sys.argv:
    add()
elif '-r' in sys.argv:
    remove()
elif '-l' in sys.argv:
    setList()
elif '-c' in sys.argv:
    check()
else:
    print('Unknown operation: {}'.format(sys.argv))