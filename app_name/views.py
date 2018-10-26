import os

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Model

app_name = 'app_name'
# app_name = '{{ app_name }}'

class OverView(generic.ListView):

    template_name = os.path.join(app_name, 'list.html')
    model = Model
    # context_object_name = '{{ model_name }}s'

class CreateModelView(generic.CreateView):

    template_name = os.path.join(app_name, 'create.html')
    model = Model
    fields = "__all__"
    success_url = reverse_lazy('app_name:overview')

class UpdateModelView(generic.CreateView):

    template_name = os.path.join(app_name, 'update.html')
    model = Model
    fields = "__all__"
    success_url = reverse_lazy('app_name:overview')

class ModelDetailsView(generic.DetailView):

    template_name = os.path.join(app_name, 'details.html')
    model = Model
    # context_object_name = '{{ model_name }}'

class DeleteModelView(generic.DeleteView):

    template_name = os.path.join(app_name, 'confirm_delete.html')
    model = Model
    fields = '__all__'
    success_url = reverse_lazy('app_name:overview')
