from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Performer, Practice_session
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def home(request):
    return HttpResponse("Home. /performers for list of performers. /history for list of session history")

def performers_index(request):
    performers = list(Performer.objects.values())
    if request.method == 'GET':
        return JsonResponse({"performers": performers})
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        body2 = body['performers']


@csrf_exempt
def history_index(request):
    history = list(Practice_session.objects.values())
    if request.method == 'GET':
        return JsonResponse({"practice_sessions": history})
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        body2 = body['practice_sessions']
        lengthValue = body2[0]['length']
        new_session = Practice_session(length=lengthValue, performer_id=1)
        new_session.save()
    return HttpResponse('Session History')

@csrf_exempt
def session_information(request, session_id):
    if request.method == "GET":
        session=Practice_session.objects.get(id=session_id)
        # print(session.length)
        return JsonResponse({"practice_sessions": session.length})
    if request.method == "DELETE":
        session=Practice_session.objects.get(id=session_id)
        session.delete()
    return HttpResponse('Session History by ID')

@csrf_exempt
def session_information_patch(request, session_id, new_length):
    if request.method == "PATCH":
        session=Practice_session.objects.get(id=session_id)
        new_length = Practice_session.objects.get(length=new_length)
        session.length = new_length
        session.save()


