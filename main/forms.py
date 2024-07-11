from django import forms
from django.forms.widgets import FileInput
from django.forms import TextInput
from .models import post, comments

class postForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=FileInput)
    class Meta:
        model = post
        fields = {'image','heading','description','article','category','tag'}
        widgets = {
            'heading': TextInput(attrs={
                'required' : "",
                'class': "from-control",
                'id':'home',
                'style': 'position:relative; padding: 10px;padding-inline-start: 20px;background-color: var(--bg-prussian-blue);border-radius: var(--radius-6);border: 1px solid var(--bg-carolina-blue);display: flex;justify-items: flex-end;transition: var(--transition-1);',
                'placeholder': 'Write heading of your post here.'
                }),
            'description': forms.Textarea(attrs={
                'required' : "",
                'class': "from-control",
                'id':'home',
                'style': 'position:relative; padding: 10px;padding-inline-start: 20px;background-color: var(--bg-prussian-blue);border-radius: var(--radius-6);border: 1px solid var(--bg-carolina-blue);display: flex;justify-items: flex-end;transition: var(--transition-1); width:100%; height:150px;color: var(--text-shadow-blue);font-family: var(--fontFamily-noto_sans);font-size: 1.6rem;line-height: var(--lineHeight-4);',
                'placeholder': 'Write description for your post here.'
                }),
            'article': forms.Textarea(attrs={
                'required' : "",
                'class': "from-control",
                'id':'home',
                'style': 'position:relative; padding: 10px;padding-inline-start: 20px;background-color: var(--bg-prussian-blue);border-radius: var(--radius-6);border: 1px solid var(--bg-carolina-blue);display: flex;justify-items: flex-end;transition: var(--transition-1); width:100%; height:950px;color: var(--text-shadow-blue);font-family: var(--fontFamily-noto_sans);font-size: 1.6rem;line-height: var(--lineHeight-4);',
                'placeholder': 'Write body of your post here.'
                }), 
            
            
        }
    


class commentForm(forms.ModelForm):
    class Meta:
        model = comments    
        fields = {'comment'}
        widgets = {
            'comment': TextInput(attrs={
                'required' : "",
                'class': "form-control",
                'style': 'max-width: 1000px; max-height:50px',
                'placeholder': 'Write your comment'
                }),
            
        }

