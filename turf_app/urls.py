from django.urls import path
from .import views

urlpatterns=[
    path("",views.index),
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
    path("viewbooking/", views.viewbooking),
    path("loadturfdetails/", views.loadturfdetails),
    path("search/", views.search),
    path("search2/", views.search2),
    path("adminviewbooking/", views.adminviewbooking),
    path("managerviewbooking/", views.managerviewbooking),
    path("membership/", views.membership),
    path("basicmember/", views.basicmember),
    path("premiummember/", views.premiummember),
    path("elitemember/", views.elitemember)


]