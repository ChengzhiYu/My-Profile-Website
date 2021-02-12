from django.shortcuts import render
from django.forms import modelformset_factory
from base.models import Contact


def home(request):
    ContactFormSet = modelformset_factory(Contact, fields='__all__')
    if request.method =="POST":
        formset = ContactFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = ContactFormSet()
    return render(request, 'base/index.html', {'formset': formset})

