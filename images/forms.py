# -*- coding: UTF-8 -*-

from django import forms

from models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title"]
