""" main """
import os
import subprocess
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
    print('\t                   No argument, shows list contents.')
    print('\t       -l          Same as no argument, Lists out list content.')
    print('\t       -h          Shows this dialog.')
    print('\t       -c          Check/uncheck list.')
    print('\t       -s List     Sets which todo list to use.')
    print('\t       -a Content  Adds an entry to your todo list.')
    print('\t       -r Index    Removes an entry from your todo list.')
    print('')

def add():
    try:
        file = open(c.filepath+c.filename, 'a+')
        file.write('\n-[]'+sys.argv[2])
        file.close()
    except:
        print("Could not add entry to list.\nExiting...\n")
        raise SystemExit

def display():
    try:
        print('')
        file = open(c.filepath+c.filename, 'r')
        i = 0
        for line in file:
            i += 1
            print(str("{}   ".format(i)+line.strip("\n")))
        file.close()
        print('')
    except:
        print("Could not display list contents.\nExiting...\n")
        raise SystemExit

def check():
    file = open(c.filepath+c.filename, 'r')
    i = 0
    for line in file:
        i += 1
        if i == int(sys.argv[2]):
            newline = line
            print(newline)
    file.close()
    setline = newline.replace("-[]", "-[x]")
    print(setline)
    subprocess.call(["sed", "-i", "-e", "s///g", c.filepath+c.filename])

def remove():
    pass

def setList():
    pass

if len(sys.argv) > 3:
    print('Too many arguments!')
    raise SystemExit

if len(sys.argv) <= 1 or '-l' in sys.argv:
    display()
    raise SystemExit # prevent display from being ran twice, see bottom of file
elif '-h' in sys.argv:
    helpme()
    raise SystemExit # prevent display from being ran twice, see bottom of file
elif '-a' in sys.argv:
    add()
elif '-r' in sys.argv:
    remove()
elif '-s' in sys.argv:
    setList()
elif '-c' in sys.argv:
    check()
    #raise SystemExit # prevent display from being ran twice, see bottom of file
else:
    print('Unknown operation: {}'.format(sys.argv))

display()
raise SystemExit