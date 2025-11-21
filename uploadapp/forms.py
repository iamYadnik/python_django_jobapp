from django import forms
from .models import Uploads, Upload_file

class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = '__all__'
        

class FileForm(forms.ModelForm):
    class Meta:
        model = Upload_file
        fields = '__all__' 