from django.shortcuts import render
import subprocess

from cowsay.models import SubmittedText
from cowsay.forms import SubmittedTextForm

# Create your views here.


def index(request):
    
    html = 'index.html'
    if request.method == 'POST':
        form = SubmittedTextForm(request.POST)
       
        if form.is_valid():
            data = form.cleaned_data
            SubmittedText.objects.create(
                input_text=data['input_text']
            )
            
            cowput = subprocess.check_output(['cowsay', data['input_text']], shell=True)
            
    form = SubmittedTextForm()

    return render(request, html, {'form': form, 'cowput': cowput})


def history(request):
    return render(request, 'history.html')
    pass

