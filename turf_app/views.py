from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")
def adminturflogin(request):
    return render(request,"adminturflogin.html")

def adminlogcheck(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/adminhomepage/")
        else:
            return redirect("/adminturflogin/")

def adminhomepage(request):
    return render(request,"adminhomepage.html")

def viewmanager(request):
    v = managertbl.objects.all()
    return render(request,"viewmanager.html",{"v":v})

def addmanager(request):
    return render(request,"addmanager.html")

def savemanager(request):
    s = managertbl()
    s.fname = request.POST.get("fname")
    s.mname = request.POST.get("mname")
    s.lname = request.POST.get("lname")
    s.gender = request.POST.get("gender")
    s.dob = request.POST.get("dob")
    s.phoneno = request.POST.get("phoneno")
    s.email = request.POST.get("email")
    s.basicsal = request.POST.get("basicsal")
    s.address = request.POST.get("address")
    s.user = request.POST.get("user")
    s.password = request.POST.get("password")
    s.save()
    return redirect("/viewmanager/")

def managerlogin(request):
    return render(request,"managerlogin.html")

def managerlogcheck(request):
    username = request.POST.get("user")
    password = request.POST.get("password")
    if managertbl.objects.filter(user=username,password=password).exists():
        v = managertbl.objects.get(user=username,password=password)
        request.session['i'] = v.id
        return redirect("/managerhomepage/")
    else:
        return HttpResponse('Invalid Data')

def managerhomepage(request):
    return render(request,"managerhomepage.html")

def managerprofile(request):
    d = managertbl.objects.get(id=request.session['i'])
    return render(request,"managerprofile.html",{'d': d})

def passchangemanager(request):
    p = managertbl.objects.get(id=request.session['i'])
    return render(request,"passchangemanager.html",{'p': p})

def updatepass(request):
    u = managertbl.objects.get(id=request.session['i'])
    u.password = request.POST.get("password")
    u.save()
    return redirect("/managerprofile/")

def addturf(request):
    return render(request,"addturf.html")

def saveturf(request):
    t = turftbl()
    t.tname = request.POST.get("tname")
    t.loc = request.POST.get("loc")
    t.timing = request.POST.get("timing")
    t.contact = request.POST.get("contact")
    t.email = request.POST.get("email")
    image = request.FILES["image"]
    im = FileSystemStorage()
    a = im.save(image.name, image)
    a1 = im.url(a)
    t.image = a1
    t.services = request.POST.get("services")
    t.amenities = request.POST.get("amenities")
    t.save()
    return redirect("/turfpage/")

def turfpage(request):
    v = turftbl.objects.all()
    return render(request,"turfpage.html",{"v":v})

def editturf(request, id):
    e = turftbl.objects.get(id=id)
    return render(request,"editturf.html", {"e": e})

def updateturf(request, id):
    u = turftbl.objects.get(id=id)
    u.tname = request.POST.get("tname")
    u.loc = request.POST.get("loc")
    u.timing = request.POST.get("timing")
    u.contact = request.POST.get("contact")
    u.email = request.POST.get("email")
    image = request.FILES["image"]
    im = FileSystemStorage()
    a = im.save(image.name, image)
    a1 = im.url(a)
    u.image = a1
    u.services = request.POST.get("services")
    u.amenities = request.POST.get("amenities")
    u.save()
    return redirect("/turfpage/")

def editmanager(request, id):
    e = managertbl.objects.get(id=id)
    return render(request,"editmanager.html", {"e": e})

def updatemanager(request, id):
    u = managertbl.objects.get(id=id)
    u.fname = request.POST.get("fname")
    u.mname = request.POST.get("mname")
    u.lname = request.POST.get("lname")
    u.gender = request.POST.get("gender")
    u.dob = request.POST.get("dob")
    u.phoneno = request.POST.get("phoneno")
    u.email = request.POST.get("email")
    u.basicsal = request.POST.get("basicsal")
    u.address = request.POST.get("address")
    u.user = request.POST.get("user")
    u.save()
    return redirect("/viewmanager/")

def deleteturf(request, id):
    u = turftbl.objects.get(id=id)
    u.delete()
    return redirect("/turfpage/")

def deletemanager(request, id):
    u = managertbl.objects.get(id=id)
    u.delete()
    return redirect("/viewmanager/")

def userlogin(request):
    return render(request, "userlogin.html")

def userregister(request):
    return render(request, "userregister.html")

def saveuser(request):
    s = usertbl()
    s.fname = request.POST.get("fname")
    s.gender = request.POST.get("gender")
    s.dob = request.POST.get("dob")
    s.phoneno = request.POST.get("phoneno")
    s.email = request.POST.get("email")
    s.username = request.POST.get("username")
    s.password = request.POST.get("password")
    s.save()
    return redirect("/userlogin/")

def userlogcheck(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if usertbl.objects.filter(username=username, password=password).exists():
        v = usertbl.objects.get(username=username, password=password)
        request.session['i'] = v.id
        return redirect("/userhomepage/")
    else:
        return HttpResponse('Invalid Data')

def viewuser(request):
    v = usertbl.objects.all()
    return render(request,"viewuser.html",{"v":v})

def deleteuser(request, id):
    u = usertbl.objects.get(id=id)
    u.delete()
    return redirect("/viewuser/")

def userhomepage(request):
    v = turftbl.objects.all()[:3]
    return render(request, "userhomepage.html", {"v": v})

def userprofile(request):
    d = usertbl.objects.get(id=request.session['i'])
    return render(request,"userprofile.html",{'d': d})

def edituser(request, id):
    e = usertbl.objects.get(id=id)
    return render(request,"edituser.html", {"e": e})

def updateuser(request, id):
    u = usertbl.objects.get(id=id)
    u.fname = request.POST.get("fname")
    u.gender = request.POST.get("gender")
    u.dob = request.POST.get("dob")
    u.phoneno = request.POST.get("phoneno")
    u.email = request.POST.get("email")
    u.username = request.POST.get("username")
    u.save()
    return redirect("/userprofile/")

def passchangeuser(request):
    p = usertbl.objects.get(id=request.session['i'])
    return render(request,"passchangeuser.html",{'p': p})

def updatepassuser(request):
    u = usertbl.objects.get(id=request.session['i'])
    u.password = request.POST.get("password")
    u.save()
    return redirect("/userprofile/")

def bookturf(request,id):
    v = turftbl.objects.get(id=id)
    s = usertbl.objects.get(id=request.session['i'])
    return render(request, "bookturf.html", {"v": v,"s":s})

def viewturf(request):
    v = turftbl.objects.all()[:3]
    return render(request, "viewturf.html", {"v": v})

def savebooking(request):
    s = bookingtbl()
    s.fname = request.POST.get("fname")
    s.contact = request.POST.get("contact")
    s.email = request.POST.get("email")
    s.tname = request.POST.get("tname")
    s.loc = request.POST.get("loc")
    s.services = request.POST.get("services")
    s.bookdate = request.POST.get("bookdate")
    s.getin = request.POST.get("getin")
    s.getout = request.POST.get("getout")
    s.items = request.POST.get("items")
    s.save()
    return redirect("/userhomepage/")

def viewbooking(request):
    v = bookingtbl.objects.all()
    return render(request,"viewbooking.html",{"v":v})

def loadturfdetails(request):
    v = turftbl.objects.all()
    return render(request, "loadturfdetails.html", {"v": v})

def search(request):
    s = request.POST.get("search")
    if turftbl.objects.filter(tname=s):
        v = turftbl.objects.filter(tname=s)
        return render(request,"viewturf.html",{"v":v})
    elif turftbl.objects.filter(loc=s):
        v = turftbl.objects.filter(loc=s)
        return render(request, "viewturf.html", {"v": v})
    elif turftbl.objects.filter(services=s):
        v = turftbl.objects.filter(services=s)
        return render(request, "viewturf.html", {"v": v})
    else:
        return HttpResponse("Invalid Data")

def search2(request):
        s = request.POST.get("search")
        if turftbl.objects.filter(tname=s):
            v = turftbl.objects.filter(tname=s)
            return render(request, "loadturfdetails.html", {"v": v})
        elif turftbl.objects.filter(loc=s):
            v = turftbl.objects.filter(loc=s)
            return render(request, "loadturfdetails.html", {"v": v})
        elif turftbl.objects.filter(services=s):
            v = turftbl.objects.filter(services=s)
            return render(request, "loadturfdetails.html", {"v": v})
        else:
            return HttpResponse("Invalid Data")

def adminviewbooking(request):
    v = bookingtbl.objects.all()
    return render(request,"adminviewbooking.html",{"v":v})

def membership(request):
    return render(request, "membership.html")

def basicmember(request):
    return render(request, "basicmember.html")

def premiummember(request):
    return render(request, "premiummember.html")

def elitemember(request):
    return render(request, "elitemember.html")

def managerviewbooking(request):
    v = bookingtbl.objects.all()
    return render(request,"managerviewbooking.html",{"v":v})