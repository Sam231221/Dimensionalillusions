from django.urls import path, re_path

from .views import (
    AboutView,
    ContactView,
    EmailSubscriptionView,
    HomeView,
    LogoutView,
    PrivacyPolicy,
    ServiceView,
    SignInView,
    SignUpView,
    TermsOfUse,
    YoMamaBotView,
)

#b'de8c1d79cd3126fb38de2e8d31bfcaf3f369f9c6ed72b46f9a'
app_name = "Ehub"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    re_path(r'^66d2b8f4a09cd35cb23076a1da5d51529136a3373f70b122/?$', YoMamaBotView.as_view()), 
    path("email-subscription/", EmailSubscriptionView.as_view(), name="email-subscription"),
    path("services/", ServiceView.as_view(), name="services"),    
    path("about-us/", AboutView.as_view(), name="about-us"),
    path("contact-us/", ContactView.as_view(), name="contact-us"),
    path("privacy-policy/", PrivacyPolicy.as_view(), name="privacy-policy"),
    path("termsofuse/", TermsOfUse.as_view(), name="termsofuse"),
    # Authentication
    path("account/sign-in/", SignInView.as_view(), name="sign-in"),
    path("account/sign-up/", SignUpView.as_view(), name="sign-up"),
    path("account/logout/", LogoutView.as_view(), name="logout"),
]
