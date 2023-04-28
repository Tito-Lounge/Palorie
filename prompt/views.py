from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from palorie.generate import generateCSV
from django.views.decorators.csrf import csrf_exempt

def home(request):
  template = loader.get_template('prompt.html')
  return HttpResponse(template.render())

def error(request):
  template = loader.get_template('error.html')
  return HttpResponse(template.render())

def newEntry(request):
  template = loader.get_template('newEntry.html')
  return HttpResponse(template.render())

@csrf_exempt # Couldn't figure out how to get CSRF protection working. Temporary workaround for testing -- don't do this in production.
def process_form(request):
  if request.method == 'POST':
    input = request.POST.get('input')
    output = generateCSV(input)
    if output == 'ERR No API key found':
      return redirect(reverse('error'))
    else:
      return redirect(reverse('newEntry'))
  else:
      template = loader.get_template('error.html')
      return HttpResponse(template.render())
  
