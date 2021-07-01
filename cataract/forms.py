from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(widget=forms.FileInput(attrs={'class': 'file-upload-btn'}), label="Upload")
