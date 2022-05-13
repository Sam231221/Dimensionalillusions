from django import forms
from .models import *
from mptt.forms import TreeNodeChoiceField

class CourseCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=CSComment.objects.all())
#this function 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
   
        self.fields['parent'].label = ''
        self.fields['parent'].required = False #to remove input required atttribute for parent so its gonna be optional

        self.fields['content'].label = ''#remove the label element for parent(text wont appear)

        self.fields['topic'].widget.attrs.update( {'class': 'd-none'})  
        self.fields['topic'].required = False   
        self.fields['topic'].label = ''
    class Meta:
        model = CSComment
        fields = ( 'parent', 'topic', 'content')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'col-sm-12'}),
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder':'Your Comment'}),
        }

    def save(self, *args, **kwargs):
        CSComment.objects.rebuild()
        return super(CourseCommentForm, self).save(*args, **kwargs)