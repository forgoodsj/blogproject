from django import forms

from .models import Img


class ImgForm(forms.ModelForm):
    image = forms.ImageField()