from django.http import HttpResponse 

'''
Created on Aug 23, 2014

@author: gwq
'''
def hello(request):
    
    i = request.GET.get('dd')
    print (i)
    print (i)
    return HttpResponse('hello,Gwq')