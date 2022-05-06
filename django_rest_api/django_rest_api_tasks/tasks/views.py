from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import TaskSerializer
from .models import Tasks

@csrf_exempt

def tasks(request):

    if(request.method == 'GET'):
        tasks = Tasks.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        print(serializer.is_valid(), 'agaba======')
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 400)

def task_detail(request, pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except:
        return HttpResponse(status=400)

    if(request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif(request.method == 'DELETE'):
        task.delete()
        return HttpResponse(status=204)









        



# Create your views here.



