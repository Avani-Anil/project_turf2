from django.urls import path
from .import views

urlpatterns=[
    path("",views.index),
    path("termsofuse/", views.termsofuse),
    path("adminturflogin/", views.adminturflogin),
    path("adminlogcheck/", views.adminlogcheck),
    path("adminhomepage/", views.adminhomepage),
    path("viewmanager/", views.viewmanager),
    path("addmanager/", views.addmanager),
    path("savemanager/", views.savemanager),
    path("managerlogin/", views.managerlogin),
    path("managerlogcheck/", views.managerlogcheck),
    path("managerhomepage/", views.managerhomepage),
    path("managerprofile/", views.managerprofile),
    path("passchangemanager/", views.passchangemanager),
    path("updatepass/", views.updatepass),
    path("turfpage/", views.turfpage),
    path("addturf/", views.addturf),
    path("saveturf/", views.saveturf),
    path("editturf/<id>", views.editturf),
    path("updateturf/<id>", views.updateturf),
    path("editmanager/<id>", views.editmanager),
    path("updatemanager/<id>", views.updatemanager),
    path("deleteturf/<id>", views.deleteturf),
    path("deletemanager/<id>", views.deletemanager),
    path("userlogin/", views.userlogin),
    path("userregister/", views.userregister),
    path("saveuser/", views.saveuser),
    path("userlogcheck/", views.userlogcheck),
    path("viewuser/", views.viewuser),
    path("deleteuser/<id>", views.deleteuser),
    path("userhomepage/", views.userhomepage),
    path("userprofile/", views.userprofile),
    path("edituser/<id>", views.edituser),
    path("updateuser/<id>", views.updateuser),
    path("passchangeuser/", views.passchangeuser),
    path("updatepassuser/", views.updatepassuser),
    path("bookturf/<id>", views.bookturf),
    path("viewturf/", views.viewturf),
    path("savebooking/", views.savebooking),
    path("usermembership/", views.usermembership),
    path("viewbooking/", views.viewbooking),
    path("generate_pdf/", views.generate_pdf),
    path("loadturfdetails/", views.loadturfdetails),
    path("search/", views.search),
    path("search2/", views.search2),
    path("adminviewbooking/", views.adminviewbooking),
    path("managerviewbooking/", views.managerviewbooking),
    path("membership/", views.membership),
    path("membershipdetails/", views.membershipdetails),
    path("viewuser1/", views.viewuser1),
    path("deleteuser1/<id>", views.deleteuser1),
    path("adminturfview/", views.adminturfview),
    path("admindeleteturf/<id>", views.admindeleteturf),
    path("review/", views.review),
    path("saverating/", views.saverating),
    path("viewrating/", views.viewrating),
    path("deleterating/<id>", views.deleterating),
    path("turfreview/<id>", views.turfreview),
    path("saveturfrating/<id>", views.saveturfrating),
    path("viewturfrating/", views.viewturfrating),
    path("viewturfrating2/", views.viewturfrating2),
    path("cancellation/", views.cancellation),
    path("adminviewcancellation/", views.adminviewcancellation),
    path("managerviewcancellation/", views.managerviewcancellation),
    path("acceptterms/", views.acceptterms),
    path("privacypolicy/",views.privacypolicy),
    path("adminviewprivacy/", views.adminviewprivacy),
    path("managerviewprivacy/", views.managerviewprivacy),
    path("paymenthandler/",views.paymenthandler),
    path("deletebooking/<id>", views.deletebooking),
    path("weather", views.weather),
    path("livescore", views.livescore),
    path("check_appointment/",views.check_appointment),
    path("userview_review/<id>",views.userview_review)



]
