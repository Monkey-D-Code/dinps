from django.urls import path
from . import views
urlpatterns = [

    path('' , views.home , name='home'),
    path('aboutus/' , views.AboutUs , name='aboutus'),
    path('admission/', views.Admission , name='admission'),
    path('course/' , views.Course , name='course'),
    path('management/', views.Management , name='management'),
    path('gallery/', views.Gallery , name='gallery'),
    path('contactus/', views.ContactUs , name='contactus'),
]
