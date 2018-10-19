---------
**Punct**
---------
.. image:: https://travis-ci.org/runarsf/punct.svg?branch=master
    :target: https://travis-ci.org/runarsf/punct
    :alt: Newest build
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg?
    :target: https://opensource.org/licenses/MIT
    :alt: License
.. image:: https://pypip.in/v/punct/badge.png
    :target: https://pypi.org/project/punct/
    :alt: PyPI version

Punct is a simple shell application to manage all your todo-lists, made in python.

Prerequisites
-------------

- Python 3.7.0 or higher
- pip 18.1 (Python 3.7.0) or higher
- Packages::

	Standard:
	    os, sys, getpass

Installation
------------

- Initial install::

    pip install punct

- Updating::

    pip install --upgrade punct

Usage
-----

 ``punct [args]``

 -h            Help dialog.
 -v            Version.
 -l            Shows list contents.
               Executes on no argument as well.
 -c Index      Check/Uncheck list item.
 -r Index      Remove list item.
 -a Content    Add an entry to the bottom of your list.
 			   Start content with '++' to add PRI tag.
 -p            Purge all completed tasks.
 			   Creates a backup file with the purged tasks.
 -d            Deletes all completed tasks. Irreversible.
 -m            Merge list and list-backup, deleting the backup.
 -e Index      Toggle entry elevation. Add/remove PRI tag.
