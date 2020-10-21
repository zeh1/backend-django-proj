from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseForbidden

from proj.settings import SECRET_KEY as SECRET

# csrf is not an issue with jwt's
from django.views.decorators.csrf import csrf_exempt

# TODO: add tests





# TODO: put functions its own module ----------------------------------------------
import json, bcrypt, jwt, datetime
from api.models import Users

def get_body_as_json(http_request_body):
    body_as_string = http_request_body.decode()
    body_as_dict = json.loads(body_as_string)
    return body_as_dict

def retrieve_username(body_as_dict):
    return str(body_as_dict["username"])

def retrieve_password(body_as_dict):
    return str(body_as_dict["password"])

def retrieve_email(body_as_dict):
    return str(body_as_dict["email"])

def get_user(username):
    user = Users.objects.get(username = username)
    return user

def create_user(username, password, email):
    new_user = Users(username = username, password = password, email = email)
    new_user.save()

def get_token_as_string(username, joined):
    payload = {
        'username': username,
        'joined': joined,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    token = jwt.encode(payload, SECRET, algorithm='HS256').decode()
    return token
# --------------------------------------------------------------------------------





@csrf_exempt
def login(request):

    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        body = get_body_as_json(request.body)
        username = retrieve_username(body)
        password = retrieve_password(body)
    except:
        return HttpResponseBadRequest()

    try:
        user = get_user(username)
    except:
        return HttpResponseNotFound()

    # TODO: implement bcrypt
    if user.password != password:
        return HttpResponseForbidden()
    
    joined = user.joined.__str__()
    token = get_token_as_string(username, joined)
    response = JsonResponse({'token': token})
    return response
#





@csrf_exempt
def signup(request):

    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    try:
        body = get_body_as_json(request.body)
        username = retrieve_username(body)
        password = retrieve_password(body)
        email = retrieve_email(body)
    except:
        return HttpResponseBadRequest()

    try:
        create_user(username, password, email)
    except:
        return HttpResponseForbidden()

    joined = get_user(username).joined.__str__()
    token = get_token_as_string(username, joined)
    response = JsonResponse({'token': token})
    return response
#





# q = request.GET.get('q')