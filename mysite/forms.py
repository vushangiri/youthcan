from django import forms
from .models import Contact, Newsletter

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key in self.Meta.required:
            self.fields[key].required = True
    class Meta:
        model = Contact
        fields = '__all__'
        required = [
            'name',
            'email',
            'subject',
            'message'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control valid",
                'id': "name", 
                'type': "text", 
                'onfocus': "this.placeholder = ''", 
                'onblur': "this.placeholder = 'Enter your name'", 
                'placeholder': "Enter your name"
            }),
            'email': forms.TextInput(attrs={
                'class': "form-control valid",
                'id': "email", 
                'type': "email", 
                'onfocus': "this.placeholder = ''", 
                'onblur': "this.placeholder = 'Enter email address'", 
                'placeholder': "Email"
            }),
            'subject': forms.TextInput(attrs={
                'class': "form-control",
                'id': "subject", 
                'type': "text", 
                'onfocus': "this.placeholder = ''", 
                'onblur': "this.placeholder = 'Enter Subject'", 
                'placeholder': "Enter Subject"
            }),
            'message': forms.Textarea(attrs={
                'class': "form-control w-100",
                'id': "message",
                'cols': "30", 
                'rows': "9", 
                'onfocus': "this.placeholder = ''", 
                'onblur': "this.placeholder = 'Enter Message'", 
                'placeholder': " Enter Message",
                'style': 'resize:none;'
            })
        }