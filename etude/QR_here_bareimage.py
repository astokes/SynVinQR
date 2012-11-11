# QR_here.py displays the current URL encoded as a QR image.  

import os, sys, inspect

#
# Much ugly bother to work with a local copy of pyqrcode
#
curpath = os.path.split(inspect.getfile(inspect.currentframe()))[0]
newpath = os.path.join(curpath, "../pyqrcode-read-only")
cmd_folder = os.path.realpath(os.path.abspath(newpath))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)
try:
    import pyqrcode
except ImportError:
    print "you need to run the script to obtain the pyqrcode module"
    sys.exit (1)
 
import bottle
import pymongo
import StringIO

print "binding to wildcard route at http://yourhost/"
@bottle.route('<path:re:.*>')   # all-route regex wildcard
def index(path): 
    # path does not contain scheme, hostname, or port 
    route_URL = 'http://' + path 

    URL = bottle.request.url 

    from pymongo import Connection
    connection = Connection('localhost', 27017)
    # pyqrcode bails out if URL string is shorter than http:/
    img = pyqrcode.MakeQRImage(URL, rounding = 0, fg = "black", bg = "burlywood", br = False)

    bottle.response.set_header('Content-type', 'image/png')

    img_buff = StringIO.StringIO()
    img.save(img_buff, format='png')
    img_buff.seek(0)

    return img_buff.read() 

bottle.run(host='0.0.0.0', port=8800)

