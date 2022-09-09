from dataclasses import fields
from django import forms
from memory.models import Memory
class MemoryForm(forms.ModelForm):
    class Meta:
        model=Memory
        fields=["title","content","memory_image"]
        
        
