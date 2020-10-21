from django.shortcuts import render

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.http import HttpResponseNotAllowed, HttpResponseNotFound, JsonResponse

# csrf is not an issue with jwt's not stored in cookies
from django.views.decorators.csrf import csrf_exempt

from api.models import Posts, Replies, Users

import jwt

from proj.settings import SECRET_KEY as SECRET

# TODO: import proj.helpers as helpers
import auth_.views as helpers



@csrf_exempt
def posts(request):
    
    if request.method == 'POST':
        
        try:
            body = helpers.get_body_as_json(request.body)
            token = helpers.retrieve_token(body)
            title = helpers.retrieve_title(body)
            post = helpers.retrieve_body(body)
        except:
            return HttpResponseBadRequest()

        try:
            payload = jwt.decode(token, SECRET, algorithms='HS256')
            user_id = payload["user_id"]
            username = payload["username"]
        except: 
            return HttpResponseForbidden()

        try:
            user = Users(pk=user_id)
            new_post = Posts(user_id=user, title=title, body=post)
            new_post.save()
        except:
            return HttpResponseForbidden()


    elif request.method == 'GET':
        
        offset = int(request.GET.get('offset'))

        if offset == None:
            offset = 0

        posts = Posts.objects.all()[offset:offset+15]
        results = []

        for entry in posts:
            o = {
                'post_id': entry.pk,
                'username': entry.user_id.username,
                'user_id': entry.user_id.pk,
                'title': entry.title,
                'body': entry.body,
                'date': entry.date.__str__(),
                'upvotes': entry.upvotes,
                'downvotes': entry.downvotes
            }
            results.append(o)
        
        results = {
            'posts': results
        }

        return JsonResponse(results)


    else:
        return HttpResponseNotAllowed(['GET, POST'])
    
    
    return HttpResponse('reached the end')



@csrf_exempt
def post(request, post_id):

    # handle GET/DELETE/PATCH for a single post

    return HttpResponse('hi')




@csrf_exempt
def replies(request, post_id):

    # handle GET/POST

    return HttpResponse(post_id)




@csrf_exempt
def reply(request, post_id, reply_id):

    # handle GET/DELETE/PATCH for a single reply

    return HttpResponse(reply_id)