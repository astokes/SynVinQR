# QR_here.py displays the current URL encoded as a QR image.  
 
import bottle
import pymongo

print "binding to wildcard route at http://yourhost/"
@bottle.route('<:re:.*>')   # all-route regex wildcard
def index(): 
	from pymongo import Connection
	connection = Connection('localhost', 27017)
	return "<html><body>Hello, %s!</body></html>" % item['name']

bottle.run(host='0.0.0.0', port=8800)

