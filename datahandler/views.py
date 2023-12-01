from django.shortcuts import render,redirect
from .forms import JsonFileUploadForm
from .models import PromptData
import json

# Create your views here.

def upload_json(request):
    if request.method == "POST":
        form = JsonFileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            for json_file in request.FILES.getlist('json_files'):
                data = json.load(json_file)
                PromptData.objects.create.create(prompt_json = data)
            return redirect('data_list')
    else:
        form = JsonFileUploadForm()
    return render(request, 'upload_json.html',{'form': form})

def data_list(request):
    data_objects = PromptData.objects.all()
    return render(request, 'data_list.html',{'data_objects':data_objects})