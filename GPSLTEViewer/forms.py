from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField (
        label='Choose your file'
    )