from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import Todoserial




#views
@api_view(['GET'])
def allurls(request):
    app_urls = {
    "URLS":"",
    "listall":'list/',
    "taskDetail":'task_detail/<str:id>/',
    "createTask":'createTask/',
    "update_task":'update_task/<str:id>/',
    "delete_task":'delete_task/<str:id>/',

    }
    return Response(app_urls)

@api_view(['GET'])
def listall(request):
    taskobj = Todoserial(Todo.objects.all().order_by('id') , many = True)
    return Response(taskobj.data)


@api_view(['GET'])
def taskDetail(request , id):
    taskobj = Todoserial(Todo.objects.get(id = id)  , many = True)
    return Response(taskobj.data)


@api_view(['POST'])
def createTask(request):
    taskobj = Todoserial(data = request.data)
    if taskobj.is_valid():
        taskobj.save()


        return Response(taskobj.data)
    return Response({"message":"Unabble to update"})

@api_view(['PUT'])
def updatetask(request , id):
    update_data = Tod.objects.get(id = id)
    taskobj = Todoserial(instance = update_data , data = request.data)
    if taskobj.is_valid():
        taskobj.save()

        return Response(taskobj.data)

    Response({"message":"UNABLE TO UPDATE"})

@api_view(['DELETE'])
def deleteTask(request , id):
    del_data = Todo.objects.get(id = id)
    del_data.delete()


    return Response("deleted Successfully ")
