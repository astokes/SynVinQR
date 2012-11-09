loaded = True
try:
    import PIL
    import Image
except ImportError:
    loaded = False

if not loaded: 
    print "PIL or Image not found"
else:
    print "PIL version", Image.VERSION
 

