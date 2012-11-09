#import os
#import sys
#print os.uname ()
#print sys.platform

import platform
import socket

host = socket.gethostbyaddr(socket.gethostname())[0]
print "Host", host, "running", platform.system(), platform.release()


