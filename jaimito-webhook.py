from itty import *  
import urllib2  
import json  
  
def sendSparkGET(url):  
    request = urllib2.Request(url,  
                            headers={"Accept" : "application/json",  
                                     "Content-Type":"application/json"})  
    request.add_header("Authorization", "Bearer "+bearer)  
    contents = urllib2.urlopen(request).read()  
    return contents  
 
def sendSparkPOST(url, data):  
    request = urllib2.Request(url, json.dumps(data),  
                            headers={"Accept" : "application/json",  
                                     "Content-Type":"application/json"})  
    request.add_header("Authorization", "Bearer "+bearer)  
    contents = urllib2.urlopen(request).read()  
    return contents  

@post('/')  
def index(request):  
    webhook = json.loads(request.body)  
    print webhook['data']['id']  
    result = sendSparkGET('https://api.ciscospark.com/v1/messages/{0}'.format(webhook['data']['id']))  
    result = json.loads(result)  
    print result  
    msg = None  
    if webhook['data']['personEmail'] != bot_email:  
        if 'batman' in result.get('text', '').lower():  
            msg = "I'm Batman!"  
        elif 'batcave' in result.get('text', '').lower():  
            msg = "The Batcave is silent..."  
        elif 'batsignal' in result.get('text', '').lower():  
            msg = "NANA NANA NANA NANA"  
        if msg != None:  
            print msg  
            sendSparkPOST("https://api.ciscospark.com/v1/messages", {"roomId": webhook['data']['roomId'], "text": msg})  
  
bearer = "NWViMTdmYzEtOTNjMC00M2NhLThiZTYtZDBkNTI4YzJmNGMxZjBjMDY2YzAtYTBl" 
bot_email = "jaimito@sparkbot.io"
  
run_itty(server='wsgiref', host='0.0.0.0', port=10010)

