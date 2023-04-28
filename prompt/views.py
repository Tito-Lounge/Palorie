from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from palorie.generate import generateCSV

def home(request):
  template = loader.get_template('prompt.html')
  return HttpResponse(template.render())

def process_form(request):
  if request.method == 'POST':
    input = request.POST.get('input')
    output = generateCSV(input)
    if output == 'ERR No API key found':
      return (request, 'failure.html')
    return render(request, 'success.html')
  else:
    return render(request, 'prompt.html')