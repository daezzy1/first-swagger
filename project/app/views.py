from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics

@csrf_exempt
def update_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def task_list(request):
    status = request.GET.get('status')
    if status == 'done':
        tasks = Task.objects.filter(completed=True)
    elif status == 'not_done':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()

    context = {
        'tasks': tasks,
        'status': status,
    }

    return render(request, 'task_list.html', context)


class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
