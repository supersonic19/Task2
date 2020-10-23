from django.shortcuts import render
from main import models
from django.views.generic import (
    CreateView,
    ListView,
    DetailView
)
# Create your views here.

class info_view(CreateView):
    model = models.info
    fields = '__all__'
    template_name = 'index.html'
    success_url = '/'

'''class message_view(ListView):
    model = models.Message.objects.latest('message')
    fields = '__all__'
    template_name = 'message.html'
    context_object_name = 'text'  
    '''
