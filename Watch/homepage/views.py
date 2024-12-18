from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import watches,WatchesUpload
from .forms import UploadForm

def Home(request):
    watches=WatchesUpload.objects.all()
    context={'watches_t':watches}
    return render(request,'home.html',context)
def About(request):
    return render(request,'about.html')
def Upload(request):
    if request.method == 'POST' :
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else :
        form=UploadForm()
    

    return render(request,'WatchUpload.html',{'form':form})

