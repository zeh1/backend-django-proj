from django.shortcuts import render

from django.http import HttpResponse

# csrf exempt for api testing
from django.views.decorators.csrf import csrf_exempt



# REMOVE DECORATOR FOR PRODUCTION
@csrf_exempt
def login(request):
    
    # login takes in user and pw in http body as json
    # validate username and pw
    # return token in json in http body, or return empty string if invalid

    # login should only accept post calls
    # TODO: return a proper http response code
    if request.method != 'POST':
        return HttpResponse('error')

    body = request.body

    return HttpResponse(body)
#



# REMOVE DECORATOR FOR PRODUCTION
@csrf_exempt
def signup(request):

    # signup takes in user pw and email in http body as json
    # validate user for uniqueness
    # create user in db
    # return token if success, else return empty string if invalid
    
    return HttpResponse('hi')
#



# q = request.GET.get('q')