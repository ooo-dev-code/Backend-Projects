from django import forms
from .models import Homework, Classes

class Create_Homework(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['subject', 'due_date', 'content']
        
class Create_Class(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ['subject', 'date', 'teacher']