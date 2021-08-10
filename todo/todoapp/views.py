from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from todoapp import serializers

# API overview
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

""" View all tasks"""
@api_view(['GET'])
def taskList(request):
    tasks = Task.object.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

""" View single task """
@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.object.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

""" Update task """
@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.object.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

""" Create Task"""
@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return redirect('list')
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.object.get(id=pk)
    task.delete()
    return Response("Task deleted successfully")