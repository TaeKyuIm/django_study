from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):# 값을 입력받는 class 만듬
    class Meta:
        model = Photo
        fields = (
            'title',
            'author',
            'image',
            'description',
            'price',
        )