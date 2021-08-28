from django import forms
from .models import Schoolapp

class SchoolappForm(forms.ModelForm):
    class Meta:
        model = Schoolapp
        fields = ['title', 'body', 'image','tags']

        widgets = {
            'body': forms.Textarea(
            attrs={'placeholder': '학교 생활을 공유해주세요.'}),
        }