from django import forms
from .models import Tasks
import re
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['difficulty', 'classes', 'themes']
        widget = {
            'difficulty': forms.Select(attrs={'class': 'form-control'}),
            'classes': forms.Select(attrs={'class': 'form-control'}),
            'themes': forms.SelectMultiple(attrs={'class': 'form-control'})
        }