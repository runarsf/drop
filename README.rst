---------
**Punct**
---------

    Punct is a simple shell application to manage all your todo-lists, made in python.

Prerequisites
-------------

- Python 3.7.0 or higher
- pip 18.1 (Python 3.7.0) or higher
- Packages::

	Standard:
	    os, sys, getpass, shutil

Installation
------------

- Initial install::

    pip install punct

- Updating::

    pip install --upgrade punct

Usage
-----

 -l            Shows list contents.
               Executes on no argument as well.
 -h            Help dialog.
 -c Index      Check/Uncheck list item.
 -r Index      Remove list item.
 -a Content    Add an entry to the bottom of your list.
 -p            Purge all completed tasks. 
 			   Creates backup file with the purged tasks.
 -d            Deletes all completed tasks. Irreversible.