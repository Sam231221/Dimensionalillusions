from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.views.generic import TemplateView, View

from .forms import ContactForm, EmailSubscriptionForm
from .models import Contact, EmailSubscription


# Custom Error Handlers
def response404_error_handler(request, exception=None):
    return render(request, "404error.html")


def response500_error_handler(request, exception=None):
    return render(request, "500error.html")


class EmailSubscriptionView(View):
    def post(self, request):
        emailform = EmailSubscriptionForm(request.POST)
        if emailform.is_valid():
            getemail = request.POST.get("email")
            email, created = EmailSubscription.objects.get_or_create(email=getemail)
            print(email)
            if created:
                styling = "style='display:flex;justify-content:center;padding:14rem;' "
                message = "<h1 class='align-center' " + styling + ">Email Subscibed!</h1>"
                return HttpResponse(message)
            else:
                styling = "style='display:flex;justify-content:center;padding:14rem;' "
                message = "<h1 class='align-center' " + styling + ">Email Already Subscibed!</h1>"
                return HttpResponse(message)


class HomeView(TemplateView):
    template_name = "frontendbase.html"


class AboutView(TemplateView):
    template_name = "about-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["emailform"] = EmailSubscriptionForm()
        return context


class ServiceView(TemplateView):
    template_name = "services.html"

class ContactView(View):
    def get(self, request):
        emailform = EmailSubscriptionForm()
        contactform = ContactForm()
        context = {
            "contactform": contactform,
            "emailform": emailform,
        }
        return render(request, "contact-us.html", context)

    def post(self, request):
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)
            contact.save()
            print(email)
            return HttpResponseRedirect(request.META["HTTP_REFERER"])


class PrivacyPolicy(TemplateView):
    template_name = "privacypolicy.html"


class TermsOfUse(TemplateView):
    template_name = "termsofuse.html"


# REGISTRATION AND LOGIN SECTION
class SignInView(View):
    def get(self, request):
        return render(request, "Authentication/sign-in.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.error(request, "User not found")
            return redirect("Ehub:sign-in")

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Wrong password")
            return redirect("Ehub:sign-in")

        login(request, user)
        return redirect("Ehub:home")


class SignUpView(View):
    def get(self, request):
        return render(request, "Authentication/sign-up.html")

    def post(self, request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        try:
            if User.objects.filter(username=username).first():
                messages.error(request, "Username is taken.")
                return redirect("Ehub:sign-up")

            if User.objects.filter(email=email).first():
                messages.error(request, "Email is taken.")
                return redirect("Ehub:sign-up")

            if password1 == password2:
                user_obj = User(username=username, email=email)
                user_obj.set_password(password1)
                user_obj.save()

                return redirect("Ehub:sign-in")
            else:
                messages.error(request, "Sorry,Password1 and Password2 did not match.")

        except Exception as e:
            print(e)


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logout successfully")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
