from django import forms
from .models import *
from mptt.forms import TreeNodeChoiceField

class FrameworkCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=FrameworkComment.objects.all())
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update( {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['content'].label = ''
        self.fields['parent'].required = False 
        self.fields['topic'].widget.attrs.update( {'class': 'd-none'})  
        self.fields['topic'].required = False   
        self.fields['topic'].label = ''
        
    class Meta:
        model = FrameworkComment
        fields = ( 'parent', 'topic', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder':'Your Comment'}),
        }

    def save(self, *args, **kwargs):
        FrameworkComment.objects.rebuild()
        return super(FrameworkCommentForm, self).save(*args, **kwargs)