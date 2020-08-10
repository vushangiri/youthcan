from .models import Admin
from .forms import ApplyForm

def add_variable_to_context(request):
    if Admin.objects.filter(active=True).exists():
        data = Admin.objects.get(active=True)
        application = ApplyForm()
                
        context = { 

            'data': data,
            'application': application

        }
        return context
    else:
        return {}
 