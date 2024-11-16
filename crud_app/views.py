from django.shortcuts import render, redirect

from .models import Contact

from .forms import *
# Create your views here.

#creating CRUD views here

#create
def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('contact_list')

    else:
        form=ContactForm()

        return render(request,'create_contact.html',{'form':form})

# read
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request,'contact_list.html',{'contacts':contacts})

# update
def update_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contact_list')

    else:
        form=ContactForm(instance=contact)

        return render(request,'update_contact.html',{'form':form})

# delete
def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('contact_list')
