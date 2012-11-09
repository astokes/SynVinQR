pymongo_loaded = True
try:
    import pymongo 
except ImportError:
    pymongo_loaded = False

if not pymongo_loaded: 
    print "pymongo not found"
else:
    print "pymongo version", pymongo.version

