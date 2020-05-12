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
            
            cowput = subprocess.check_output(['cowsay', str(data['input_text'])]).decode("utf-8")
            form = SubmittedTextForm()
            return render(request, html, {'form': form, 'cowput': cowput})
            
    form = SubmittedTextForm()

    return render(request, html, {'form': form})


def history(request):
    last_ten = SubmittedText.objects.all().order_by('-id')[:10]
    return render(request, 'history.html', {'last_ten': last_ten})

    

