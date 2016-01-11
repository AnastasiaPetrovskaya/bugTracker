from django.shortcuts import render
from django.views.generic import ListView
from .models import Ticket
from django.http import HttpResponse

# Create your views here.

def BugListView(ListView):
    #model = Ticket
    #print 0
    #template_name = 'list.html'
    return HttpResponse("You're looking at question %s.")

class index(ListView):
    model = Ticket
    print 0
    template_name = 'ticket_list.html'

