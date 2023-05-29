from django.shortcuts import render
from .models import Departments,Doctors
from .forms import BookingForm

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept = {
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)

def doctor(request):
    dict_docs = {
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs )

def booking(request):
    if request.method == 'POST' :
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form ={
        'form':form
    }
    return render(request,'booking.html',dict_form)
# Create your views here.
