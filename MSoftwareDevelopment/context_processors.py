from .models import Framework

def frameworks(request):
    return {'frameworks':Framework.objects.all()}