from .models import Admin

def add_variable_to_context(request):
    
    data = Admin.objects.get(active=True)
            
    context = { 

        'data': data

    }
    return context
 