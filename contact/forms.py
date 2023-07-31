from django.forms import forms,ModelForm
from .models import ContactFrom

class ContactFrom(ModelForm):
    class Meta:
        model = ContactFrom
        fields = '__all__'
