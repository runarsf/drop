# -*- coding: utf-8 -*-


"""punct.punct: provides entry point main()."""


__version__ = "1.1.5"


import os
import sys
import shutil

from .config import Conf

path = (os.path.dirname(os.path.realpath(__file__)))

def verify():
    if not os.path.exists(Conf("path")):
        try:
            print("Creating file directory")
            os.makedirs(Conf("path"))
        except:
            print("Could not create directory. Check config formatting.\nExiting...")
            raise SystemExit
    if not os.path.isfile(Conf("path")+Conf("file")):
        try:
            print("Creating file")
            file = open(Conf("path")+Conf("file"), 'w+')
            file.close()
        except:
            print("Could not create file. Check config formatting.\nExiting...")
            raise SystemExit
verify()

def helpme():
    print('\n\tUsage: punct [arguments]\n')
    print('\t                   No argument, shows list contents.')
    print('\t       -l          Same as no argument, Lists out list content.')
    print('\t       -h          Shows this dialog.')
    # print('\t       -s List     Sets which todo list to use.')
    # print('\t       -f Path     Sets list dir (folder)')
    print('\t       -c Index    Check/uncheck list item.')
    print('\t       -r Index    Remove list item.')
    print('\t       -a Content  Add an entry to the bottom of your list.')
    print('\t       -p          Purge all completed tasks.\n\
                            Creates backup file with the purged tasks.')
    print('\t       -d          Deletes all completed tasks. Irreversible.')
    print('')

def add():
    try:
        file = open(Conf("path")+Conf("file"), 'a+')
        file.write('\n-[]'+sys.argv[2])
        file.close()
    except:
        print("Could not add entry to list.\nExiting...\n")
        raise SystemExit

def display():
    try:
        f = open(Conf("path")+Conf("file"), 'r')
        l = [l for l in f.readlines() if l.strip()]
        f.close()
        f = open(Conf("path")+Conf("file"), 'w+')
        f.writelines( l )
        f.close()
    except:
        print("Could not remove whitespace from list contents.\nExiting...\n")
        raise SystemExit
    finally:
        print('')
        file = open(Conf("path")+Conf("file"), 'r')
        i = 0
        for line in file:
            i += 1
            print(str("{}   ".format(i)+line.strip("\n")))
        file.close()
        print('')

def check():
    with open(Conf("path")+Conf("file"), 'r') as file:
        data = file.readlines()
        if data[int(sys.argv[2])-1][:3] == "-[]":
            data[int(sys.argv[2])-1] = data[int(sys.argv[2])-1].replace("-[]", "-[x]")
        else:
            data[int(sys.argv[2])-1] = data[int(sys.argv[2])-1].replace("-[x]", "-[]")
        with open(Conf("path")+Conf("file"), 'w') as file:
            file.writelines( data )


def remove():
    with open(Conf("path")+Conf("file"), 'r') as file:
        data = file.readlines()
        data[int(sys.argv[2])-1] = ""
        with open(Conf("path")+Conf("file"), 'w') as file:
            file.writelines( data )

# def setList():
#     file = open('config.py', 'r')
#     i = 0
#     for line in file:
#         i += 1
#         if "filename" in line:
#             with open('config.py', 'r') as file:
#                 data = file.readlines()
#                 data[i-1] = "\nfilename='{}'\n".format(sys.argv[2])
#                 with open('config.py', 'w') as file:
#                         file.writelines( data )
#                 file.close()

#                 f = open('config.py', 'r')
#                 l = [l for l in f.readlines() if l.strip()]
#                 f.close()
#                 f = open('config.py', 'w+')
#                 f.writelines( l )
#                 f.close()

# def setFolder():
#     file = open('config.py', 'r')
#     i = 0
#     for line in file:
#         i += 1
#         if "filepath" in line:
#             with open('config.py', 'r') as file:
#                 data = file.readlines()
#                 data[i-1] = "\nfilepath='{}'\n".format(sys.argv[2])
#                 with open('config.py', 'w') as file:
#                         file.writelines( data )
#                 file.close()

#                 f = open('config.py', 'r')
#                 l = [l for l in f.readlines() if l.strip()]
#                 f.close()
#                 f = open('config.py', 'w+')
#                 f.writelines( l )
#                 f.close()

def purge():
    bad_words = ['-[x]']

    with open(Conf("path")+Conf("file")) as oldfile, open(Conf("path")+Conf("file")+".tmp", 'w') as tempfile, open(Conf("path")+Conf("file")+".bak", "a") as bakfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                tempfile.write(line)
            elif any(bad_word in line for bad_word in bad_words):
                bakfile.write(line)
    with open(Conf("path")+Conf("file")+".tmp") as f:
        with open(Conf("path")+Conf("file"), "w") as f1:
            for line in f:
                f1.write(line)
    f.close()
    f1.close()
    tempfile.close()
    bakfile.close()
    os.remove(Conf("path")+Conf("file")+".tmp")

def delete():
    bad_words = ['-[x]']

    with open(Conf("path")+Conf("file")) as oldfile, open(Conf("path")+Conf("file")+".tmp", 'w') as tempfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                tempfile.write(line)
    with open(Conf("path")+Conf("file")+".tmp") as f:
        with open(Conf("path")+Conf("file"), "w") as f1:
            for line in f:
                f1.write(line)
    f.close()
    f1.close()
    tempfile.close()
    os.remove(Conf("path")+Conf("file")+".tmp")

if len(sys.argv) > 3:
    print('\nToo many arguments!\nTip:\n    Enclosing text in quotation marks makes it one argument.\n')
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
elif '-d' in sys.argv:
    delete()
# elif '-s' in sys.argv:
#     setList()
#     raise SystemExit
# elif '-f' in sys.argv:
#     setFolder()
#     raise SystemExit
elif '-c' in sys.argv:
    check()
    #raise SystemExit # prevent display from being ran twice, see bottom of file
elif '-p' in sys.argv:
    purge()
else:
    print('Unknown operation: {}'.format(sys.argv))

display()
raise SystemExit
