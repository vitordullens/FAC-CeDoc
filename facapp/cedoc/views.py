from django.shortcuts import render, redirect
from .models import Doc, TextFile
from .forms import ImageUpload, TextUpload, AudioUpload, VideoUpload
from facapp.settings import MEDIA_ROOT
import os

# Create your views here.

def index(request):
    data = {}
    data['files'] = Doc.objects.all()
    return render(request, 'cedoc/index.html', data)

def option(request):
    return render(request, 'cedoc/option.html')

def new_entry(request, btn):
    data = {}
    form = ""
    if(btn == 'text'):
        form = TextUpload(request.POST or None, request.FILES or None)
        data['file'] = "TEXT"
    elif(btn == 'image'):
        form = ImageUpload(request.POST or None, request.FILES or None)
        data['file'] = "IMAGE"
    elif(btn == 'video'):
        form = VideoUpload(request.POST or None, request.FILES or None)
        data['file'] = "VIDEO"
    else:
        form = AudioUpload(request.POST or None, request.FILES or None)
        data['file'] = "AUDIO"
    if form.is_valid():
        form.save()
        return redirect('url_index')
    data['form'] = form
    return render(request, 'cedoc/new_entry.html', data)

def delete(request, pk):
    doc = Doc.objects.get(pk=pk)
    if(doc.fileType == '.txt' or doc.fileType == '.md' or doc.fileType == '.pdf'):
        text = TextFile.objects.get(pk=pk).File
        os.remove(os.path.join(MEDIA_ROOT, str(text)))
    doc.delete()
    return redirect('url_index')