from django import forms
from .models import WatchesUpload

class UploadForm(forms.ModelForm):
    class Meta:
        model = WatchesUpload
        fields = ['name','description','price','image']
