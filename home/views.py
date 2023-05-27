from django.shortcuts import render



def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def department(request):
    return render(request,'department.html')

def doctor(request):
    return render(request,'doctors.html' )

def booking(request):
    return render(request,'booking.html')
# Create your views here.
