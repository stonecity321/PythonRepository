from TasksManager.models import Task
from django.http import HttpResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
# We import the csrf_exempt decorator that we will use to line 4.
import json
   # We import the json module we use to line 8.


def task_detail(request, pk):
    check_task =  Task.objects.filter(id = pk)
    try:
        task = check_task.get()
    except (Task.DoesNotExist, Task.MultipleObjectsReturned):
        return HttpResponseRedirect(reverse('public_empty'))
        request.session['last_task'] = task.id
    return render(request, 'TasksManager/task_detail.html', {'object': task})