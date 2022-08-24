from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Performer

# Create your views here.



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

# def performers_index(request):
#     if request.method == 'GET':
#         performers = Performer.objects.all()
#         # return JsonResponse({"performer": performers })
#         print("test")
#         return HttpResponse("Test")

# def practice_sessions_history(request, performer_id)