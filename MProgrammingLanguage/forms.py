from django import forms
from .models import *
from mptt.forms import TreeNodeChoiceField

class PlcommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=PLComment.objects.all())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(  
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['content'].label = ''
        self.fields['parent'].required = False
        self.fields['topics'].widget.attrs.update( {'class': 'd-none'})  
        self.fields['topics'].required = False   
        self.fields['topics'].label = ''
    class Meta:
        model = PLComment
        fields = ( 'parent', 'topics', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder':'Your Comment'}),
        }

    def save(self, *args, **kwargs):
        PLComment.objects.rebuild()
        return super(PlcommentForm, self).save(*args, **kwargs)