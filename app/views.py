from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request,'app/index.html')

def saveUser(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = Users.objects.filter(Email=email)
        if user:
            message = "User already exists"
            return render(request,"app/index.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = Users.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = "User registered successfully, Please sign in"
                return render(request,"app/login.html",{'msg':message})


def Login(request):
    return render(request,"app/login.html")

# def userlogin(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         print(email,password)

#         myuser = authenticate(request, Password=password)
#         print(myuser)

#         if myuser is not None:
#             login(request, myuser)
#             # messages.success(request, 'successfully logged in')
#             return render(request,'app/about.html')
#         else:
#             message = 'invalid credentials'
#             return render(request,'app/login.html',{'msg':message})


def userlogin(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = Users.objects.get(Email=email)
        print(user.values())
        if user:
            if user.Password == password:
                request.session['fname']=user.Firstname
                return render(request,'app/about.html')
            else:
                message = 'invalid credentials'
                return render(request,'app/login.html',{'msg':message})
        else:
            message = 'Please enter correct email'
            return render(request,'app/login.html',{'msg':message})
        
def userlogout(request):
    logout(request)
    return render(request,'app/index.html')



