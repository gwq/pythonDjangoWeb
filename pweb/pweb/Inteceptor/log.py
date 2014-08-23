import time
'''
Created on Aug 24, 2014

@author: gwq
'''
class LogRecord:
    
    def process_request(self,request):
        print time.strftime('%Y-%m-%d %H:%I:%S',time.localtime(time.time())),
        print (request.META['REMOTE_ADDR'])
