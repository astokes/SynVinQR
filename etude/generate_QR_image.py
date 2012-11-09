# Simple program to call pyqrcode to generate a URL based QR code image 
# and save the generated image to disk 

# The generated QR image was tested with a Samsung Galaxy II running the 
# Norton Snap QR Code Reader from the Android Play Store 

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



URL = 'https://education.10gen.com/courses/10gen/M101/2012_Fall/'
image = 'image/generate_QR_image.png'

qr_image = pyqrcode.MakeQRImage(URL, rounding = 0, fg = "black", bg = "burlywood", br = False)
qr_image.save(image)

print "Test QR image saved to", image

# the following command runs ImageMagick on my system to display the image in a Window
# qr_image.show()

