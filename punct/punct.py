# -*- coding: utf-8 -*-


"""punct.punct: provides entry point main()."""


__version__ = "1.2.1"


import os
import sys

from .config import Conf

tabsize = Conf('tabsize')
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
    print('\n\tUsage: punct [args]\n')
    print('\t       -h          Shows this dialog.')
    print('\t       -v          Version.')
    print('\t       -l          Shows list contents.\n\
                           └ Executes on no argument as well.')
    print('\t       -c Index    Check/uncheck list item.')
    print('\t       -r Index    Remove list item.')
    print('\t       -a Content  Add an entry to the bottom of your list.\n\
                           └ Start content with \'++\' to add PRI tag.')
    print('\t       -p          Purge all completed tasks.\n\
                           └ Creates backup file with the purged tasks.')
    print('\t       -d          Deletes all completed tasks. Irreversible.')
    print('\t       -m          Merge list and list-backup, deleting backup.')
    print('\t       -e Index    Toggle entry elevation. Add/remove PRI tag.')
    print('')

def add():
    try:
        file = open(Conf("path")+Conf("file"), 'a+')
        if len(sys.argv) <= 2:
            file.write('\n-[]'+userInput(">>> "))
        else:
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
        print('\n\t[{}]\n'.format(Conf("file")).expandtabs(int(tabsize/1.2)))
        file = open(Conf("path")+Conf("file"), 'r')
        sp = "  "
        i = 0
        for line in file:
            i += 1
            st = "   "
            if line[:6] == "-[x]++" or line[:5] == "-[]++":
                line = line.replace("++", "")
                st = "PRI"
            if i > 9:
                sp = " "
            elif i > 99:
                sp = ""
            if "-[x]" in line:
                line = line.replace("-[x]", "[x] ")
                print(str("\t{0}{1})  {2}  ".format(i, sp, st)+'\u0336'.join(line).strip("\n") + '\u0336').expandtabs(int(tabsize)))
            else:
                line = line.replace("-[]", "[ ] ")
                print(str("\t{0}{1})  {2}  ".format(i, sp, st)+line.strip("\n")).expandtabs(int(tabsize)))
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

def elevate():
    with open(Conf("path")+Conf("file"), 'r') as file:
        data = file.readlines()
        if data[int(sys.argv[2])-1][:5] == "-[]++" or data[int(sys.argv[2])-1][:6] == "-[x]++":
            data[int(sys.argv[2])-1] = data[int(sys.argv[2])-1].replace("-[]++", "-[]")
        else:
            data[int(sys.argv[2])-1] = data[int(sys.argv[2])-1].replace("-[]", "-[]++")
        with open(Conf("path")+Conf("file"), 'w') as file:
            file.writelines( data )

def remove():
    with open(Conf("path")+Conf("file"), 'r') as file:
        data = file.readlines()
        if data[int(sys.argv[2])-1][:6] == "-[x]++" or data[int(sys.argv[2])-1][:5] == "-[]++":
            if userConfirm("Are you sure you want to delete tagged entry?"):
                data[int(sys.argv[2])-1] = ""
        else:
            data[int(sys.argv[2])-1] = ""
        with open(Conf("path")+Conf("file"), 'w') as file:
            file.writelines( data )

def purge():
    bad_words = ['-[x]']

    if userConfirm("Are you sure?"):
        with open(Conf("path")+Conf("file")) as oldfile, open(Conf("path")+Conf("file")+".tmp", 'w') as tempfile, open(Conf("path")+Conf("file")+".bak", "a") as bakfile:
            for line in oldfile:
                if not any(bad_word in line for bad_word in bad_words):
                    tempfile.write(line)
                elif any(bad_word in line for bad_word in bad_words):
                    bakfile.write(line+"\n")
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

    if userConfirm("Are you sure? This action is irreversible."):
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

def merge():
    if userConfirm("Are you sure?"):
        if not os.path.isfile(Conf("path")+Conf("file")+".bak"):
            print("\nNo backup file found!\n")
            raise SystemExit
        if not os.path.isfile(Conf("path")+Conf("file")):
            print("\nTodo-file not found!\n")
            raise SystemExit
        with open(Conf("path")+Conf("file"), "a") as mainfile, open(Conf("path")+Conf("file")+".bak", "r") as bakfile:
            for line in bakfile:
                mainfile.write("\n{}".format(line))
        mainfile.close()
        bakfile.close()
        os.remove(Conf("path")+Conf("file")+".bak")

def userConfirm(word):
    yes = ['Y', '']
    no = ['n']

    print(word + " " + \
        str(yes).replace("', '", "/").replace("['", "[").replace("']", "") + \
        str(no).replace("', '", "/").replace("['", "").replace("']", "]"))
    choice = input().lower()
    if choice in str(yes).lower():
       return True
    elif choice in no:
       return False
    else:
       raise TypeError
       return False

def userInput(word):
    print(word)
    choice = input()
    return choice

if len(sys.argv) > 3:
    print('\nToo many arguments!\nTip:\n    Enclosing text in quotation marks makes it one argument.\n')
    raise SystemExit
elif len(sys.argv) <= 1 or '-l' in sys.argv:
    display()
    raise SystemExit # prevent display from being run twice
elif '-h' in sys.argv:
    helpme()
    raise SystemExit # prevent display from being run
elif '-c' in sys.argv:
    check()
elif '-r' in sys.argv:
    remove()
elif '-a' in sys.argv:
    add()
elif '-p' in sys.argv:
    purge()
elif '-d' in sys.argv:
    delete()
elif '-m' in sys.argv:
    merge()
elif '-e' in sys.argv:
    elevate()
elif '-v' in sys.argv:
    print("\nYou are running punct v{}.\n".format(__version__))
    raise SystemExit
else:
    print('\nUnknown operation: {}\n'.format(sys.argv))
    raise SystemExit

display()
raise SystemExit
