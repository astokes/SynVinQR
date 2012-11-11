# WEEK1 
# to amass working examples of most of the form elements needed 
# by the SynVin data input pages 

import bottle
import pymongo
from bottle import request

print "binding master form to http:/" 
@bottle.route('/') 
def index():
	return bottle.template ('form_elements')

print "binding form to http://text/"
@bottle.post('/text') 
def text_form():
        Q = request.forms.question 
	A = request.forms.answer
	return "<html><body>Text form submitted<br/>Q:%s<br/>A:%s</body></html>" % (Q, A)

print "binding to http://yourhost/password"
@bottle.post('/password')
def password_form(): 
	P = request.forms.password
	return "<html><body>Trending upward in the Google Zeitgeist: %s</body></html>" % P 

print "binding to http://yourhost/radiobutton"
@bottle.post('/radiobutton')
def radio_form(): 
	# contains logic to prove we remember cookie elsewhere 
	G = request.forms.sex
	S = request.get_cookie('purience', G)
	pronoun = ['his', 'her'][G=='female']
	return "<html><body>The human %s signals %s desires indirectly.</body></html>" % ( 
          S, pronoun)

# patterned after WEEK1 Bottle framework: using cooki" %" % P
# eliminates problem with user unable to refresh POST requests
# CONTROLLER side
print "binding to http://yourhost/radcook"
@bottle.post('/radcook')
def radcook_form(): 
	P = request.forms.purience
	bottle.response.set_cookie('purience',P)
	bottle.redirect('/show_radcook')
# 
# VIEW side
@bottle.route('/show_radcook')
def show_radcook(): 
	P = request.get_cookie('purience') 
	return "<html><body>You're a %s, and we'll not forget it!</body></html>" % P


print "binding to http://yourhost/checkbox"
@bottle.post('/checkbox')
def checkbox_form(): 
	OS = request.forms.getall('phoneOS')
	OS.insert (0, 'Your landline')  
	# deprecate everything, picking on the last item only 
	return "<html><body>%s is obsolete and outdated.</body></html>" % OS [len(OS)-1]

bottle.run(host='0.0.0.0', port=8800)

