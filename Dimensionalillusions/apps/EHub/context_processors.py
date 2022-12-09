from .forms import EmailSubscriptionForm


def forms(request):
    return {"emailform": EmailSubscriptionForm()}
