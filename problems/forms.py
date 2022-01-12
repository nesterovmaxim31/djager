from django import forms
from .models import List2, List3, List4, List5

class List2_Forms(forms.ModelForm):
    class Meta:
        model = List2
        fields = ('title', 'link', 'code', 'slug', 'explanation')
        widgets = {'code': forms.TextInput, 'explanation': forms.TextInput}

class List3_Forms(forms.ModelForm):
    class Meta:
        model = List3
        fields = ('title', 'link', 'code', 'slug', 'explanation')

class List4_Forms(forms.ModelForm):
    class Meta:
        model = List4
        fields = ('title', 'link','text', 'code', 'slug', 'explanation')
    
class List5_Forms(forms.ModelForm):
    class Meta:
        model = List5
        fields = ('title', 'link','text', 'code', 'slug', 'explanation')
        

