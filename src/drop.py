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
import config as c

def helpme():
    print('\n\tUsage: python3 drop.py [arguments]\n')
    print('\t       *           No argument, shows list contents.')
    print('\t       -l          Same as no argument, Lists out list content.')
    print('\t       -h          Shows this dialog.')
    print('\t       -c          Check/uncheck list.')
    print('\t       -s List     Sets which todo list to use.')
    print('\t                   Creates it if not existing.')
    print('\t       -a Content  Adds an entry to your todo list.')
    print('\t       -r Index    Removes an entry from your todo list.')
    print('')

def add():
    try:
        fileAdd = open(c.filepath+c.filename, 'a+')
        fileAdd.write('\n-[]'+sys.argv[2])
        fileAdd.close()
        #print(c.filepath+c.filename)
        #print('-[]'+sys.argv[2])
    except:
        print("Could not add entry to list.\nExiting...\n")
        raise SystemExit

def display():
    try:
        print('')
        fileRead = open(c.filepath+c.filename, 'r')
        i = 0
        for line in fileRead:
            i += 1
            print(str("{}   ".format(i)+line.strip("\n")))
        fileRead.close()
        print('')
    except:
        print("Could not display list contents.\nExiting...\n")
        raise SystemExit

def check():
    pass

def remove():
    pass

def setList():
    pass

if len(sys.argv) > 3:
    print('Too many arguments!')
    raise SystemExit

if len(sys.argv) <= 1 or '-l' in sys.argv:
    display()
elif '-h' in sys.argv:
    helpme()
elif '-a' in sys.argv:
    add()
elif '-r' in sys.argv:
    remove()
elif '-s' in sys.argv:
    setList()
elif '-c' in sys.argv:
    check()
else:
    print('Unknown operation: {}'.format(sys.argv))