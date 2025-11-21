from django.shortcuts import render
from uploadapp.forms import UploadForm, FileForm

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
            return render(request, 'uploadapp/addimage.html', {'form': form, 'saved_object' : saved_object})
    else:
        form = UploadForm()
    return render(request, 'uploadapp/addimage.html', {'form': form})


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            saved_object = form.instance
            return render(request, 'uploadapp/addfile.html', {'form': form, 'saved_object' : saved_object})
    else:
        form = FileForm()
    return render(request, 'uploadapp/addfile.html', {'form': form})