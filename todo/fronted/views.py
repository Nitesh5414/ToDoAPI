from django.shortcuts import render
from todoapp.models import Task
from django.views.generic import (
    ListView,
)

# Create your views here.
# def list_view(request):
#     return render(request, 'fronted/index.html')

class TaskView(ListView):
    model = Task
    template_name = 'fronted/index.html'
