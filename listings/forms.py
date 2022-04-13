from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    
    expediteur=forms.CharField(label='Nom',widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'name'
        
    }))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={
        'class':'form-control',
        'id':'email',
         
    }))
    subject=forms.CharField(label='Sujet',widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'subject',
        
    }))
    message=forms.CharField(label='Message',widget=forms.Textarea(attrs={
       'class':'form-control',
    }))
    class Meta:
        model = Message
        fields=('expediteur','email','subject','message')
        