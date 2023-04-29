from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from palorie.generate import generateCSV
import pandas as pd
import os

# Default view. Just asks for a prompt.
def home(request):
  template = loader.get_template('prompt.html')
  return HttpResponse(template.render())

# Generic error view -- currently only used to show a lack of API key.
def error(request):
  template = loader.get_template('error.html')
  return HttpResponse(template.render())

# View for a newly generated entry.
def newEntry(request):

  # PROMPT USED: "Instead of getting a specific filepath to a CSV file, can I make it so that it outputs the most recently created file from a folder?"
  # Get a list of all CSV files in the directory, sort the list by creation time (most recent first)
  csv_files = [f for f in os.listdir('./output') if f.endswith('.csv')]
  csv_files.sort(key=lambda x: os.path.getmtime(os.path.join('./output', x)), reverse=True)
  data = pd.read_csv(os.path.join('./output', csv_files[0]))
  context = {'data' : data}
  template = loader.get_template('newEntry.html')
  return HttpResponse(template.render(context))

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
  
