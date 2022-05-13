from .models import ProgrammingLanguage

def programminglanguages(request):
    return {'programminglanguages':ProgrammingLanguage.objects.all()}