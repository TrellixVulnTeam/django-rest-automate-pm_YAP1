from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from restautomatepm.models import Projects, Phases, Log
from restautomatepm.serializers import ProjectsSerializer, PhasesSerializer, LogSerializer
from rest_framework import generics 


class ProjectList(generics.ListAPIView): 
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class CreateProject(generics.CreateAPIView): 
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

@csrf_exempt
def phases(request): 
    if request.method == "GET": 
        phases = Phases.objects.all()
        serializer = PhasesSerializer(phases, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "POST": 
        data = JSONParser().parse(request)
        serializer = PhasesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def log(request): 
    if request.method == "GET": 
        log = Log.objects.all()
        serializer = LogSerializer(log, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == "POST": 
        data = JSONParser().parse(request)
        serializer = LogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)