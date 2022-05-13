from django.urls import path

from .views import (
    AboutView,
    ContactView,
    EmailSubscriptionView,
    HomeView,
    LogoutView,
    PrivacyPolicy,
    SignInView,
    SignUpView,
    TermsOfUse,
)

app_name = "Ehub"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("email-subscription/", EmailSubscriptionView.as_view(), name="email-subscription"),
    path("about-us/", AboutView.as_view(), name="about-us"),
    path("contact-us/", ContactView.as_view(), name="contact"),
    path("privacy-policy/", PrivacyPolicy.as_view(), name="privacy-policy"),
    path("termsofuse/", TermsOfUse.as_view(), name="termsofuse"),
    # Authentication
    path("account/sign-in/", SignInView.as_view(), name="sign-in"),
    path("account/sign-up/", SignUpView.as_view(), name="sign-up"),
    path("account/logout/", LogoutView.as_view(), name="logout"),
]
