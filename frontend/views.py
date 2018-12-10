from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    data ={
        'PageTitle' : "Durgapur Institute of Nursing",
        'heading' : "Durgapur Institute of Nursing and Paramedical Science",
        'sub_heading_1' : "(College of Nursing, College of Management & College of Education)",
        'sub_heading_2' : "Supported by: INC,HNSC,KNC,WBNC,UGC,NCTE, Regd.Under West Bengal Paramedical Association",
    }
    return render(request , 'frontend/home.html' , context=data)

def AboutUs(request):
    data ={
        'PageTitle' : "About Us",
    }
    return render(request , 'frontend/about_us.html' , context=data)

def Admission(request):
    data ={
        'PageTitle' : "Admission",
    }
    return render(request , 'frontend/admission.html' , context=data)

def Course(request):
    data ={
        'PageTitle' : "Courses",
    }
    return render(request , 'frontend/course.html' , context=data)


def Management(request):
    data ={
        'PageTitle' : "Management",
    }
    return render(request , 'frontend/management.html' , context=data)

def Gallery(request):
    data ={
        'PageTitle' : "Gallery",
    }
    return render(request , 'frontend/gallery.html' , context=data)


def ContactUs(request):
    data ={
        'PageTitle' : "Contact Us",
    }
    return render(request , 'frontend/contact_us.html' , context=data)
