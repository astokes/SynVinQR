# technique discovered at 
# http://stackoverflow.com/questions/279237/python-import-a-module-from-a-folder
# which will enable me to run my local copy of pyqrcode from upward 

import os, sys, inspect
curpath = os.path.split(inspect.getfile(inspect.currentframe()))[0]
newpath = os.path.join(curpath, "../pyqrcode-read-only")
cmd_folder = os.path.realpath(os.path.abspath(newpath))
if cmd_folder not in sys.path:
    print "Adding path", cmd_folder
    sys.path.insert(0, cmd_folder)
    import pyqrcode

