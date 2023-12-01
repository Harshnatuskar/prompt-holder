from django import forms
from multiupload.fields import MultiFileField

class JsonFileUploadForm(forms.Form):
    json_files = MultiFileField(min_num=1, max_num=5, max_file_size=1024 * 1024 * 5)
