from django.shortcuts import render

from django.http import HttpResponse

# csrf exempt for api testing
from django.views.decorators.csrf import csrf_exempt

import json



# TODO: put functions in its own module
def get_body_as_json(http_request_body):
    body_as_string = http_request_body.decode()
    body_as_dict = json.loads(body_as_string)
    return body_as_dict
#
def retrieve_username(body_as_dict):
    pass
#



# TODO: REMOVE DECORATOR FOR PRODUCTION
@csrf_exempt
def login(request):
    
    # login takes in user and pw in http body as json
    # validate username and pw
    # return token in json in http body, or return empty string if invalid

    # login should only accept post calls
    # TODO: return a proper http response code; this is only a temp fix
    if request.method != 'POST':
        return HttpResponse('error')

    # retrieve body as json
    body = get_body_as_json(request.body)

    # TODO: check for existence of username and pw fields
    #       check that username and pw fields are proper types



    return HttpResponse('hi')
#



# TODO: REMOVE DECORATOR FOR PRODUCTION
@csrf_exempt
def signup(request):

    # signup takes in user pw and email in http body as json
    # validate user for uniqueness
    # create user in db
    # return token if success, else return empty string if invalid
    
    return HttpResponse('hi')
#



# q = request.GET.get('q')
# type(), type() is <>, isinstance(<>, type)