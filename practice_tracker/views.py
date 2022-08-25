from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Performer, Practice_session
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def home(request):
    return HttpResponse("Home. /performers for list of performers. /history for list of session history")

def performers_index(request):
    performers = list(Performer.objects.values())
    return JsonResponse({"performers": performers})

@csrf_exempt
def history_index(request):
    history = list(Practice_session.objects.values())

    if request.method == 'GET':
        return JsonResponse({"practice_sessions": history})
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        # print(body_unicode)
        body = json.loads(body_unicode)
        # print(body)
        # print(body['practice_sessions'])
        body2 = body['practice_sessions']
        print(body2)
        print(body2[0])
        lengthValue = body2[0]['length']
        print(lengthValue)
        new_session = Practice_session(length=lengthValue, performer_id=1)
        new_session.save()

        # data = request.body
        # decodedData = data.decode()
        # print(decodedData)
        # print(decodedData[0])
        # decodedData.save()
        # print(HttpResponse(decodedData))
        # print(JsonResponse(decodedData, safe=False))
    
    return HttpResponse('test')



    # return JsonResponse({"practice_sessions": history})

# if request.method == 'GET':
#     # THIS DOESN'T WORK YET
#     cat = Cat.objects.get(id=cat_id)
#     response = vars(cat).pop('_state')
#     return JsonResponse({ "cat" : response })
# if request.method == 'PATCH':
#     # print(request.body.name)
#     body_unicode = request.body.decode('utf-8')
#     body = json.loads(body_unicode)
#     # content = body['content']
#     print(body['name'])
#     # Get a reference to the cat
#     cat = get_object_or_404(Cat, id=cat_id)
#     # Change the cat
#     cat.name = body['name']
#     cat.age = body['age']
#     cat.description = body['description']
#     # Save the cat
#     cat.save()
#     return HttpResponse("Updated", status=200)
# if request.method == 'DELETE':
#     # Get a reference to the cat
#     cat = get_object_or_404(Cat, id=cat_id)
#     cat.delete()
#     return HttpResponse("Deleted", status=204)
