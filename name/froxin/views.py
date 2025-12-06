from django.shortcuts import render,redirect
from .models import*
# Create your views here.
def index(request):
    return render(request,'home.html')
    
def register(request):
    if request.method=='POST':
        u_name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        Register.objects.create_user(username=u_name ,email=email,password=password,usertype='user')
        return redirect('/')
    return render(request,'register.html')
