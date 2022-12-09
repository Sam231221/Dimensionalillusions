from django import forms
from django.forms import widgets
from mptt.forms import TreeNodeChoiceField

from .models import *


# Django built-in ModelForm automatically creates a model in database defining a form containing
# fields asscoiated with the model's instance fields
class ArticleCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=AComment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["parent"].widget.attrs.update({"class": "d-none"})  # remove the select option
        self.fields["parent"].label = ""
        self.fields["content"].label = ""  # remove the label element for parent(text wont appear)
        self.fields[
            "parent"
        ].required = False  # to remove input required atttribute for parent so its gonna be optional

    class Meta:
        model = AComment
        fields = ("parent", "content")

        widgets = {
            "name": forms.TextInput(attrs={"class": "col-sm-12"}),
            "content": forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Comment"}),
        }

    def save(self, *args, **kwargs):
        AComment.objects.rebuild()
        return super(ArticleCommentForm, self).save(*args, **kwargs)


"""#note forms.Form doesn't have get_cleaned_data()  and save() method """


class ArticleSearchForm(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["q"].label = ""
        self.fields["q"].widget.attrs.update({"class": "form-control", "placeholder": "Search the Articles..."})
