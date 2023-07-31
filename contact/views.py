from django.shortcuts import render,HttpResponse
from .forms import  ContactFrom
from django.core.mail import send_mail
# Create your views here.

def contact_us(request):
   if request.method == 'POST':
        form = ContactFrom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"New message from {name}"
            body = f"Name: {name}\nEmail: {email}\n\n{message}"
            recipient_email = 'pradhanakash745@gmail.com'
            send_mail(subject, body, email, [recipient_email])
            return render(request,'thankyou.html',{"name":name})
   else:
       form = ContactFrom()

   return render(request,'index.html',{'form':form})
