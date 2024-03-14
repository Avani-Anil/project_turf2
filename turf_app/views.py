import razorpay
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.gis.db.backends.postgis import const
from django.contrib.sites import requests
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template import Context
from xhtml2pdf import pisa
from .models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def termsofuse(request):
    return render(request, "termsofuse.html")


def adminturflogin(request):
    return render(request, "adminturflogin.html")


def adminlogcheck(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/admin_homepage/")
        else:
            return redirect("/adminturflogin/")


def admin_homepage(request):
    u = usertbl.objects.all().count()
    t = turftbl.objects.all().count()
    b = bookingtbl.objects.all().count()
    v = bookingtbl.objects.all()[:4]
    return render(request, "admin_homepage.html",{"v": v, "u": u, "t": t, "b": b})


def viewmanager(request):
    v = managertbl.objects.all()
    return render(request, "viewmanager.html", {"v": v})


def addmanager(request):
    return render(request, "addmanager.html")


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
    return render(request, "managerlogin.html")


def managerlogcheck(request):
    username = request.POST.get("user")
    password = request.POST.get("password")
    if managertbl.objects.filter(user=username, password=password).exists():
        v = managertbl.objects.get(user=username, password=password)
        request.session['i'] = v.id
        return redirect("/manager_homepage/")
    else:
        return HttpResponse('Invalid Data')


def manager_homepage(request):
    u = usertbl.objects.all().count()
    t = turftbl.objects.all().count()
    b = bookingtbl.objects.all().count()
    v = bookingtbl.objects.all()[:4]
    return render(request, "manager_homepage.html", {"v": v, "u": u, "t": t, "b": b})


def managerprofile(request):
    d = managertbl.objects.get(id=request.session['i'])
    return render(request, "managerprofile.html", {'d': d})


def passchangemanager(request):
    p = managertbl.objects.get(id=request.session['i'])
    return render(request, "passchangemanager.html", {'p': p})


def updatepass(request):
    u = managertbl.objects.get(id=request.session['i'])
    u.password = request.POST.get("password")
    u.save()
    return redirect("/managerprofile/")


def addturf(request):
    return render(request, "addturf.html")


def saveturf(request):
    t = turftbl()
    t.tname = request.POST.get("tname")
    t.loc = request.POST.get("loc")
    t.district = request.POST.get("district")
    t.grass = request.POST.get("grass")
    t.length = request.POST.get("length")
    t.width = request.POST.get("width")
    t.timing = request.POST.get("timing")
    t.contact = request.POST.get("contact")
    t.email = request.POST.get("email")
    image = request.FILES["image"]
    im = FileSystemStorage()
    a = im.save(image.name, image)
    a1 = im.url(a)
    t.image = a1
    t.sports = request.POST.get("sports")
    t.amenities = request.POST.get("amenities")
    t.amount = request.POST.get("amount")
    t.res_name = request.POST.get("res_name")
    t.res_number = request.POST.get("res_number")
    t.save()
    return redirect("/turfpage/")


def turfpage(request):
    v = turftbl.objects.all()
    return render(request, "turfpage.html", {"v": v})
def addresource(request):
    v = turftbl.objects.all()
    return render(request, "addresource.html", {"v": v})


def saveresource(request):
    s = resource_tbl()
    s.res_name = request.POST.get("res_name")
    s.res_number = request.POST.get("res_number")
    s.turf_id_id = request.POST.get("tname")
    s.save()
    return redirect("/resource/")

def deleteresource(request, id):
    u = resource_tbl.objects.get(id=id)
    u.delete()
    return redirect("/resource/")
def resource(request):
    v = resource_tbl.objects.all()
    return render(request, "resource.html", {"v": v})

def adminturfview(request):
    v = turftbl.objects.all()
    return render(request, "adminturfview.html", {"v": v})


def editturf(request, id):
    e = turftbl.objects.get(id=id)
    return render(request, "editturf.html", {"e": e})


def updateturf(request, id):
    u = turftbl.objects.get(id=id)
    u.tname = request.POST.get("tname")
    u.loc = request.POST.get("loc")
    u.district = request.POST.get("district")
    u.grass = request.POST.get("grass")
    u.length = request.POST.get("length")
    u.width = request.POST.get("width")
    u.timing = request.POST.get("timing")
    u.contact = request.POST.get("contact")
    u.email = request.POST.get("email")
    u.sports = request.POST.get("sports")
    u.amenities = request.POST.get("amenities")
    u.amount = request.POST.get("amount")
    u.save()
    try:
        image = request.FILES["image"]
        im = FileSystemStorage()
        a = im.save(image.name, image)
        a1 = im.url(a)
        u.image = a1
        u.save()
    except:
        pass

    return redirect("/turfpage/")

def editresource(request,id):
    e = resource_tbl.objects.get(id=id)
    return render(request, "editresource.html", {"e": e})

def updateresource(request,id):
    ur = resource_tbl.objects.get(id=id)
    ur.tname = request.POST.get("tname")
    ur.res_name = request.POST.get("res_name")
    ur.res_number = request.POST.get("res_number")
    ur.save()
    return redirect("/resource/")

def editmanager(request, id):
    e = managertbl.objects.get(id=id)
    return render(request, "editmanager.html", {"e": e})


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


def admindeleteturf(request, id):
    u = turftbl.objects.get(id=id)
    u.delete()
    return redirect("/adminturfview/")


def deletemanager(request, id):
    u = managertbl.objects.get(id=id)
    u.delete()
    return redirect("/viewmanager/")


def userlogin(request):
    return render(request, "userlogin.html")


def userregister(request):
    return render(request, "userregister.html")


def send_sms(phoneno):
        # Make an HTTP request to your SMS API
        api_key = '2f5f879c8emsh3c498feaddb2013p177f4bjsnd926154ca68b'
        api_host = 'send-sms18.p.rapidapi.com'
        message = 'Welcome to our website! Thank you for registering.'
        response = requests.post(
            'https://send-sms18.p.rapidapi.com/',
            data={'api_key': api_key, 'api_host': api_host, 'phoneno': phoneno, 'message': message}
        )
        if response.status_code == 200:
            return True
        else:
            return False


def saveuser(request):
    email = request.POST.get("email")
    phoneno = request.POST.get("phoneno")
    if usertbl.objects.filter(email=email, phoneno=phoneno).exists():
        messages.error(request, "Email and Phone No already exists")
        return redirect("/userregister/")
    s = usertbl()
    s.fname = request.POST.get("fname")
    s.mname = request.POST.get("mname")
    s.lname = request.POST.get("lname")
    s.district = request.POST.get("district")
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
    return render(request, "viewuser.html", {"v": v})


def deleteuser(request, id):
    u = usertbl.objects.get(id=id)
    u.delete()
    return redirect("/viewuser/")


def viewuser1(request):
    v = usertbl.objects.all()
    return render(request, "viewuser1.html", {"v": v})


def deleteuser1(request, id):
    u = usertbl.objects.get(id=id)
    u.delete()
    return redirect("/viewuser1/")


def userhomepage(request):
    a = usertbl.objects.get(id=request.session['i'])
    v = turftbl.objects.filter(district=a.district)[:3]
    return render(request, "userhomepage.html", {"v": v})


def userprofile(request):
    d = usertbl.objects.get(id=request.session['i'])
    return render(request, "userprofile.html", {'d': d})


def edituser(request, id):
    e = usertbl.objects.get(id=id)
    return render(request, "edituser.html", {"e": e})


def updateuser(request, id):
    u = usertbl.objects.get(id=id)
    u.fname = request.POST.get("fname")
    u.mname = request.POST.get("mname")
    u.lname = request.POST.get("lname")
    u.district = request.POST.get("district")
    u.gender = request.POST.get("gender")
    u.dob = request.POST.get("dob")
    u.phoneno = request.POST.get("phoneno")
    u.email = request.POST.get("email")
    u.username = request.POST.get("username")
    u.save()
    return redirect("/userprofile/")


def passchangeuser(request):
    p = usertbl.objects.get(id=request.session['i'])
    return render(request, "passchangeuser.html", {'p': p})


def updatepassuser(request):
    u = usertbl.objects.get(id=request.session['i'])
    u.password = request.POST.get("password")
    u.save()
    return redirect("/userprofile/")


def bookturf(request, id):
    v = turftbl.objects.get(id=id)
    s = usertbl.objects.get(id=request.session['i'])
    return render(request, "bookturf.html", {"v": v, "s": s})


def viewturf(request):
    v = turftbl.objects.all()[:3]
    return render(request, "viewturf.html", {"v": v})


razorpay_client = razorpay.Client(auth=('rzp_test_G0D8VXQvuP0UIb', 'ade6yjh3z1b80SRZcNqa9pyW'))


def savebooking(request):
    s = bookingtbl()
    s.fname = request.POST.get("fname")
    s.mname = request.POST.get("mname")
    s.lname = request.POST.get("lname")
    s.contact = request.POST.get("contact")
    s.email = request.POST.get("email")
    s.tname = request.POST.get("tname")
    s.loc = request.POST.get("loc")
    s.sports = request.POST.get("sports")
    s.bookdate = request.POST.get("bookdate")
    s.getin = request.POST.get("getin")
    s.getout = request.POST.get("getout")
    s.items = request.POST.get("items")
    s.user_id_id = request.session['i']
    s.totalamt = request.POST.get("totalamt")
    s.save()
    currency = 'INR'
    amount = int(s.totalamt) * 100

    razorpay_order = razorpay_client.order.create(dict(amount=amount, currency=currency, payment_capture='0'))

    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler'

    context = {}
    context['razorpay_order_id'] = razorpay_order_id

    context['razorpay_merchant_key'] = 'rzp_test_G0D8VXQvuP0UIb'
    context['razorpay_amount'] = amount
    context['amnt']=s.totalamt
    context['currency'] = currency
    context['callback_url'] = callback_url
    context['getin']=s.getin
    context['getout']=s.getout
    context['turf']=s.tname
    context['date']=s.bookdate

    return render(request, "summary.html", context)


def paymenthandler(request):
    amount = request.POST.get("amount")
    razorpay_order_id = request.POST.get('order_id')

    payment_id = request.POST.get('payment_id', '')
    print('paymentid:', str(payment_id))

    signature = request.POST.get('razorpay_signature', '')

    params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }

    # verify the payment signature.

    print("res:")
    amount = int(amount) * 100  # Rs. 200
    razorpay_client.payment.capture(payment_id, amount)
    return redirect("/userhomepage/")


def viewbooking(request):
    v = bookingtbl.objects.filter(user_id=request.session['i'])
    return render(request, "viewbooking.html", {"v": v})

def generate_pdf(request):
        booking_data = bookingtbl.objects.filter(user_id=request.session['i'])

        context = {'booking_data': booking_data}
        template = get_template('viewbooking.html')
        html_content = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="booking_report.pdf"'

        # Create PDF from HTML content
        pisa_status = pisa.CreatePDF(html_content, dest=response)

        if pisa_status.err:
            return HttpResponse('Error generating PDF')

        return response
def loadturfdetails(request):
    a = usertbl.objects.get(id=request.session['i'])
    v = turftbl.objects.filter(district=a.district)[:3]
    return render(request, "loadturfdetails.html", {"v": v})


def usermembership(request):
    return render(request, "usermembership.html")


def search(request):
    s = request.POST.get("search")
    if turftbl.objects.filter(tname__iexact=s):
        v = turftbl.objects.filter(tname__iexact=s)
        return render(request, "viewturf.html", {"v": v})
    elif turftbl.objects.filter(loc__iexact=s):
        v = turftbl.objects.filter(loc__iexact=s)
        return render(request, "viewturf.html", {"v": v})
    elif turftbl.objects.filter(sports__iexact=s):
        v = turftbl.objects.filter(sports__iexact=s)
        return render(request, "viewturf.html", {"v": v})
    else:
        return HttpResponse("Invalid Data")


def search2(request):
    s = request.POST.get("search")
    if turftbl.objects.filter(tname__iexact=s):
        v = turftbl.objects.filter(tname__iexact=s)
        return render(request, "loadturfdetails.html", {"v": v})
    elif turftbl.objects.filter(loc__iexact=s):
        v = turftbl.objects.filter(loc__iexact=s)
        return render(request, "loadturfdetails.html", {"v": v})
    elif turftbl.objects.filter(sports__iexact=s):
        v = turftbl.objects.filter(sports__iexact=s)
        return render(request, "loadturfdetails.html", {"v": v})
    else:
        return HttpResponse("Invalid Data")


def adminviewbooking(request):
    v = bookingtbl.objects.all()
    return render(request, "adminviewbooking.html", {"v": v})


def membership(request):
    return render(request, "membership.html")


def membershipdetails(request):
    return render(request, "membershipdetails.html")


def managerviewbooking(request):
    v = bookingtbl.objects.all()
    return render(request, "managerviewbooking.html", {"v": v})


def review(request):
    return render(request, "review.html")


def saverating(request):
    s = reviewrating_tbl()
    s.rating = request.POST.get("rating")
    s.fname = request.POST.get("fname")
    s.user_id_id = request.session['i']
    s.save()
    return redirect("/userhomepage/")


def viewrating(request):
    v = reviewrating_tbl.objects.all()
    return render(request, "viewrating.html", {"v": v})


def deleterating(request, id):
    u = turfreview_tbl.objects.get(id=id)
    u.delete()
    return redirect("/viewturfrating/")


def turfreview(request, id):
    v = turftbl.objects.get(id=id)
    return render(request, "turfreview.html", {"v": v})


def saveturfrating(request, id):
    s = turfreview_tbl()
    s.rating = request.POST.get("rating")
    s.review = request.POST.get("review")
    s.tname = request.POST.get("tname")
    s.fname = request.POST.get("fname")
    s.turf_id_id = id
    s.user_id_id = request.session['i']
    s.save()
    return redirect("/userhomepage/")


def viewturfrating(request):
    v = turfreview_tbl.objects.all()
    return render(request, "viewturfrating.html", {"v": v})


def viewturfrating2(request):
    v = turfreview_tbl.objects.all()
    return render(request, "viewturfrating2.html", {"v": v})


def cancellation(request):
    return render(request, "cancellation.html")


def adminviewcancellation(request):
    return render(request, "adminviewcancellation.html")


def managerviewcancellation(request):
    return render(request, "managerviewcancellation.html")


def acceptterms(request):
    return render(request,"acceptterms.html")


def privacypolicy(request):
    return render(request, "privacypolicy.html")

def adminviewprivacy(request):
    return render(request, "adminviewprivacy.html")

def managerviewprivacy(request):
    return render(request, "managerviewprivacy.html")

def deletebooking(request, id):
    u = bookingtbl.objects.get(id=id)
    u.delete()
    return redirect("/managerviewbooking/")

def weather(request):
    return render(request, "weather.html")

def livescore(request):
    return render(request, "livescore.html")

def check_appointment(request):
    data={}
    get_in=request.GET.get("get_in")
    b_date=request.GET.get("b_date")
    print(b_date)
    if bookingtbl.objects.filter(getin=get_in,bookdate=b_date).exists():
        data["message"]="error"
    else:
        data['message']="success"
    return JsonResponse(data)

def userview_review(request,id):
    v = turfreview_tbl.objects.filter(turf_id=id).exclude(user_id=request.session['i'])
    return render(request, "userview_review.html", {"v": v})

def searchuser(request):
    s = request.POST.get("searchuser")
    if usertbl.objects.filter(fname__iexact=s):
        v = usertbl.objects.filter(fname__iexact=s)
        return render(request, "viewuser1.html", {"v": v})
    else:
        return HttpResponse("Invalid Data")

def searchturf(request):
    s = request.POST.get("searchturf")
    if turftbl.objects.filter(tname__iexact=s):
        v = turftbl.objects.filter(tname__iexact=s)
        return render(request, "turfpage.html", {"v": v})
    elif turftbl.objects.filter(loc__iexact=s):
        v = turftbl.objects.filter(loc__iexact=s)
        return render(request, "turfpage.html", {"v": v})
    else:
        return HttpResponse("Invalid Data")

def searchbooking(request):
    s = request.POST.get("searchbooking")
    if bookingtbl.objects.filter(fname__iexact=s):
        v = bookingtbl.objects.filter(fname__iexact=s)
        return render(request, "managerviewbooking.html", {"v": v})
    elif bookingtbl.objects.filter(tname__iexact=s):
        v = bookingtbl.objects.filter(tname__iexact=s)
        return render(request, "managerviewbooking.html", {"v": v})
    else:
        return HttpResponse("Invalid Data")

def searchmanager(request):
    s = request.POST.get("searchmanager")
    if managertbl.objects.filter(fname__iexact=s):
        v = managertbl.objects.filter(fname__iexact=s)
        return render(request, "viewmanager.html", {"v": v})
    else:
        return HttpResponse("Invalid Data")

