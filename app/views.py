from django.shortcuts import render,redirect
from .models import Register
def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")
def send(request):
    name=request.POST.get("name")
    age=request.POST.get("age")
    gender = request.POST.get("gender")
    phone=request.POST.get("phone")
    id=phone[7:10]
    username=request.POST.get("username")
    password=request.POST.get("password")
    house=request.POST.get("house")
    Village=request.POST.get("Village")
    Mandal=request.POST.get("Mandal")
    Distric=request.POST.get("Distaic")
    States=request.POST.get("States")
    PinCode=request.POST.get("PinCode")
    if Register.objects.filter(username=request.POST['username']).exists():
        return render(request, "index.html", {"message": "Username existed"})
    else:
        Register(name=name, age=age, gender=gender, phone=phone, idno=id, username=username, password=password, house=house,
                 Village=Village, Mandal=Mandal, Distaic=Distric, States=States, PinCode=PinCode).save()
        return render(request, "profile.html", {"message": "Thank you For Register! Please Login"})
def login(request):
    return render(request,"login.html")

from .models import Total
def log(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    qr = Register.objects.filter(username=username)
    for i in qr:
        if i.username == username and i.password == password:
            qr = Register.objects.get(idno=i.idno)
            return render(request,"profile.html",{"qr":qr})
        elif Register.objects.filter(username=request.POST['username']).exists() and password == i.password:
            return render(request, "login.html", {"qr": "Username exists"})
        elif username != i.username and password !=i.password:
            return render(request,"login.html",{"qr": "Username exists"})
        else:
            return render(request, "login.html", {"qr": "InValied Username & Password  Please try agin"})



from django.contrib.auth import logout
from django.contrib import messages
def logout_out(request):
    messages.info(request, "Logged out successfully!")
    logout(request)
    return render(request,"index.html")


def password(request):
    return render(request,"password.html")


def getpass(request):
    phone=request.POST.get("phone")
    id=phone[7:10]
    qr=Register.objects.get(idno=id)
    # name = request.POST.get(qr.name)
    age = request.POST.get("age")
    # gender = request.POST.get(qr.gender)
    # phone = request.POST.get(phone)
    # username = request.POST.get(qr.username)
    password = request.POST.get("password")
    # house = request.POST.get(qr.house)
    # Village = request.POST.get(qr.Village)
    # Mandal = request.POST.get(qr.Mandal)
    # Distric = request.POST.get(qr.Distaic)
    # States = request.POST.get(qr.States)
    # PinCode = request.POST.get(qr.PinCode)
    Register(idno=id,age=age,password=password,name=qr.name,gender=qr.gender,username=qr.username,phone=phone,house=qr.house,Village=qr.Village,Mandal=qr.Mandal,Distaic=qr.Distaic,States=qr.States,PinCode=qr.PinCode).save()
    return render(request,"change.html",{"qr":qr})


# def change(request,pk):
#     qr=Register.objects.get(idno=pk)
#     return render(re)
