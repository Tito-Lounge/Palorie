from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from palorie.generate import generateCSV
from palorie.visualizeData import pieChart
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import datetime

# Default view. Just asks for a prompt.
def home(request):
  # Generate File Path for Most Recent
  file_path = './output'
  file_list = [f for f in os.listdir(file_path) if f.endswith('.json')]
  file_list.sort(key=lambda x: os.path.getmtime(os.path.join('./output', x)), reverse=True)
  most_recent = file_list[0]

  context = {'filename': most_recent }
  return render(request, 'prompt.html', context)

# Generic error view -- currently only used to show a lack of API key.
def error(request):
  template = loader.get_template('error.html')
  return HttpResponse(template.render())

@csrf_exempt # Couldn't figure out how to get CSRF protection working. Temporary workaround for testing -- don't do this in production.
def downloadFile(request): # FOR THE FILE IN NEWENTRY
  csv_files = [f for f in os.listdir('./output') if f.endswith('.csv')]
  csv_files.sort(key=lambda x: os.path.getmtime(os.path.join('./output', x)), reverse=True)
  file_path = os.path.join('./output', csv_files[0])
  with open(file_path, 'r') as file:
    response = HttpResponse(file, content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
  return response

@csrf_exempt 
def download_file(request, filename): # FOR THE FILES IN THE LIST OF CSVs
  file_path = os.path.join('./output', filename)
  with open(file_path, 'rb') as csv_file:
    response = HttpResponse(csv_file.read(), content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={filename}'
  return response

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
  
@csrf_exempt # Couldn't figure out how to get CSRF protection working. Temporary workaround for testing -- don't do this in production.
def entry_list(request):
  file_path = './output'
  file_list = [f for f in os.listdir(file_path) if f.endswith('.json')]
  file_list.sort(key=lambda x: os.path.getmtime(os.path.join('./output', x)), reverse=True)
  context = {'file_list' : file_list,
             'file_path' : file_path, 
             }
  return render(request, 'entry_list.html', context)

@csrf_exempt # Couldn't figure out how to get CSRF protection working. Temporary workaround for testing -- don't do this in production.
def entry_detail(request, filename):
  file_path = './output/' + filename
  # Generate dataframe from filepath
  data = pd.read_json(file_path)

  # Capitalize column names
  data.columns = data.columns.str.capitalize()
  total_calories = data['Calories'].sum()

  # Visualize nutritional data
  chart_html = pieChart(data)
  table_html = data.to_html(index=False)
  context = {'data': table_html,
             'filename' : filename,
             'pieChart' : chart_html,
             'progress' : total_calories}
  
  return render(request, 'entry_detail.html', context)