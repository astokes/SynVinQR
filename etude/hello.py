# WEEK 2
# simple pymongo web server responding to the root URL 
# with a value from a MongoDB database 
# and responding to the /hello URL by populating a template 
# with values from a literal list 

import bottle
import pymongo

print "binding to http://yourhost/"
@bottle.route('/') 
def index(): 
	from pymongo import Connection
	connection = Connection('localhost', 27017)
	db = connection.etude
	names = db.names
	item = names.find_one() 
	return "<html><body>Hello, %s!</body></html>" % item['name']

print "binding to http://yourhost/hello"
@bottle.route('/hello')
def hello(): 
	return bottle.template ('hello', names=['Montgomery', 'Hikaru', 'Nyota'] )

bottle.run(host='0.0.0.0', port=8800)

