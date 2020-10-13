from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def task_views(request):
    data = {
        'List View':'api/task/list/',
        'Detail View':'api/task/detail/',
        'Create View':'api/task/create/',
        'Update View':'api/task/update/',
        'Delete View':'api/task/delete/',
    }

    return Response(data)

@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all()
    
    if tasks.count() == 0:
        data = {'mensagem':'Nenhuma task foi registrada.'}
        return Response(data)

    task_serializer = TaskSerializer(tasks, many=True)
    
    return Response(task_serializer.data)

@api_view(['GET'])
def task_detail(request, slug):
    try:
        tasks = Task.objects.get(slug=slug)

    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    task_serializer = TaskSerializer(tasks)
    
    return Response(task_serializer.data)

@api_view(['POST', ])
def task_create(request):
    task_serializer = TaskSerializer(data = request.data)

    data = {
        'data':task_serializer.initial_data,
        'mensagem': 'Os dados não foram suficientes para criação da task.'
    }

    if task_serializer.is_valid():
        task_serializer.save()

        data['data'] = task_serializer.data
        data['mensagem'] = 'Task criada com sucesso.'

        return Response(data)
    
    data['erros'] = task_serializer.errors

    return Response(data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', ])
def task_update(request, slug):
    try:
        task = Task.objects.get(slug=slug)

    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    task_serializer = TaskSerializer(instance=task, data = request.data)

    data = {
        'data':task_serializer.initial_data,
        'mensagem':'Os dados não foram suficientes para atualização da task.'
    }

    if task_serializer.is_valid():
        task_serializer.save()

        data['data'] = task_serializer.data
        data['mensagem'] = 'Task atualizada com sucesso.'

        return Response(data, status=status.HTTP_201_CREATED)

    data['erros'] = task_serializer.errors

    return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
def task_delete(request, slug):
    try:
        task = Task.objects.get(slug=slug)

    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    task_serializer = TaskSerializer(instance=task, data = request.data)
    task.delete()

    data = {
        'data':task_serializer.data,
        'mensagem':'Task deletada com sucesso.'
    }

    return Response(data)

