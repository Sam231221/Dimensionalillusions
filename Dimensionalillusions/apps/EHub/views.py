import json
import random
import re
from pprint import pprint

import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View

from .forms import ContactForm, EmailSubscriptionForm
from .models import Contact, EmailSubscription

ACCESS_TOKEN='EAAHVSzGDb7oBAHHD4DeZA1atoTGlcGtYaS2TV6R5S5e5F4eZATZCVOIm7YmLGVpGctj8UYV3lvNMhs72aZCrRThNZBemVWE3pD604NjKe8NlhDbFJv9nhS8p38IM88MaCRtYTQ6VbLMDTWpziQKc9fch8LDS3WmR8x1D11Dv2o3WUu7lXdWcH'   #paste your token here
VERYFY_TOKEN='9867743856'

# Custom Error Handlers
def response404_error_handler(request, exception=None):
    return render(request, "utilities/404error.html")


def response500_error_handler(request, exception=None):
    return render(request, "utilities/500error.html")
from django.utils.datastructures import MultiValueDictKeyError

jokes = {
         'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                    """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
         'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                    """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
         'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                    """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
         }

def post_facebook_message(fbid, recevied_message):
    # Remove all punctuations, lower case the text and split it based on space
    tokens = re.sub(r"[^a-zA-Z0-9\s]",' ',recevied_message).lower().split()
    joke_text = ''
    for token in tokens:
        if token in jokes:
            joke_text = random.choice(jokes[token])
            break
    if not joke_text:
        joke_text = "I didn't understand! Send 'stupid', 'fat', 'dumb' for a Yo Mama joke!"    
         

    user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':ACCESS_TOKEN}
    print('user_details_params:', user_details_params)
    user_details = requests.get(user_details_url, user_details_params).json()
    print('user_details:', user_details)
    joke_text = 'Yo '+user_details['first_name']+'..!' + joke_text
    
    post_message_url = f'https://graph.facebook.com/v2.6/me/messages?access_token={ACCESS_TOKEN}'
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":joke_text}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())

class YoMamaBotView(View):

    #at client side(in facebook messenger app, we need to provide callback url i.e django url that hits this with token 9867743856)
   #if we provide correct credentials then it gets verified
    def get(self, request, *args, **kwargs):
        try:
            token=self.request.GET['hub.verify_token']
        except MultiValueDictKeyError:
            token=False

        if token=='9867743856':
            return HttpResponse(request.GET['hub.challenge'])
        else:
            return HttpResponse("Error invalid token")

    # The get method is the same as before.. omitted here for brevity
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check to make sure the received call is a message call
                # This might be delivery, optin, postback for other events 
                if 'message' in message:
                    # Print the message to the terminal
                    pprint(message)    
                    # Assuming the sender only sends text. Non-text messages like stickers, audio, pictures
                    # are sent as attachments and must be handled accordingly. 
                    post_facebook_message(message['sender']['id'], message['message']['text'])                        
        return HttpResponse()

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
