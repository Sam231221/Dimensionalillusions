from django import forms
from django.forms import ModelForm, fields

from .models import Contact, EmailSubscription


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].label = ""
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "id": "name", "placeholder": "Enter Your Name."}
        )

        self.fields["email"].label = ""
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "id": "email", "placeholder": "Enter Your Email."}
        )

        self.fields["subject"].label = ""
        self.fields["subject"].widget.attrs.update(
            {"class": "form-control", "id": "subject", "placeholder": "Subject"}
        )
        self.fields["message"].label = ""
        self.fields["message"].widget.attrs.update(
            {"class": "form-control", "id": "message", "rows": 5, "placeholder": "Your Message"}
        )


class EmailSubscriptionForm(ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ("email",)

        widgets = {
            "email": forms.EmailInput(attrs={"placeholder": "Your Email Here"}),
        }
