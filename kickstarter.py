from urllib2 import Request, urlopen, URLError  
import threading
from datetime import datetime

kickstarter_url= 'https://www.kickstarter.com/projects/levinotik/learn-functional-programming-with-lambdaschool/comments' 
amount_raised = 0
def getAmounts():
	now = datetime.now()
	print("\n")
	print ("It is now ") + now.strftime("%m-%d at %H:%M")

	req = Request(kickstarter_url)  
	try:  
	    response = urlopen(req)  
	except URLError as e:  
	    if hasattr(e, 'reason'):  
	        print 'We failed to reach a server.'  
	        print 'Reason: ', e.reason  
	    elif hasattr(e, 'code'):  
	        print 'The server couldn\'t fulfill the request.'  
	        print 'Error code: ', e.code  
	else:  
	    # this is where you put the rest of your code to run after opening the web page 
	    the_page = response.readlines()     # read each line of the html file into a variable 'the_page'  
	    for line in the_page:               # iterate through the lines  
	                                        # checking for the ones we want to find & print them  
	        if 'itemprop="Project[pledged]' in line:  
	            amount_raised = line.split('"')[14].replace("</data>", "").replace(">", "")

	# turn amount_raised to a number
	to_num = amount_raised.replace("$", "").replace(",", "")
	float_raised = float(to_num)

	print ("The kickstarter is at ${:,.2f}".format(float_raised))

	
	threading.Timer(400, getAmounts).start()

getAmounts()