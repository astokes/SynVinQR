import pymongo

connection = pymongo.Connection()
server = connection.server_info()['version']
print "mongod server version ", server 
required = "2.0.6"
if tuple(server.split('.')) < tuple(required.split('.')):
	print " **REQUIRED** version ", required 
	exit (1)

