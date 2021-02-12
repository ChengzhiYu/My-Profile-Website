from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class meta:
        model = Contact
        field = "__all__"
