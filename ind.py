from urllib2 import Request, urlopen, URLError  
import threading
from datetime import datetime

url = 'https://www.indiegogo.com/projects/secret-sauce-a-step-by-step-growth-hacking-guide--2#/backers' 

# def getAmounts():
now = datetime.now()
print("\n")
print ("It is now ") + now.strftime("%m-%d at %H:%M")

req = Request(url)  
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
    print(the_page)
    for line in the_page:               # iterate through the lines  
        if 'gogo-test-"raised"' in line:  
            amount_raised = line

print("You're raised another ${:,.2f}".format(line))
print("Hello")

# getAmounts()