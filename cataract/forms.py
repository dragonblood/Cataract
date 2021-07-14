from django import forms
from django.core.validators import FileExtensionValidator

class DocumentForm(forms.Form):

    docfile = forms.FileField(widget=forms.FileInput(attrs={'class': 'file-upload-btn'}),
                              label="Upload",
                              validators=[ FileExtensionValidator(['jpeg','png','jpg']) ],
                              required=True)

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image._size > 1*1024*1024:
                raise ValidationError("Image file too large ( > 1mb )")
            return image
        else:
            raise ValidationError("Couldn't read uploaded image")
