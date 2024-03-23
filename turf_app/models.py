from django.db import models


# Create your models here.
class managertbl(models.Model):
    fname = models.CharField(max_length=20, null=True)
    mname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=7, null=True)
    dob = models.DateField(null=True)
    phoneno = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    basicsal = models.CharField(max_length=20, null=True)
    address = models.TextField(max_length=60,null=True)
    user = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=10, null=True)

class turftbl(models.Model):
    tname = models.CharField(max_length=20, null=True)
    loc = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=20, null=True)
    grass = models.CharField(max_length=10, null=True)
    length = models.FloatField(null=True)
    width = models.FloatField(null=True)
    timing = models.CharField(max_length=20, null=True)
    contact = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(null=True, upload_to='media')
    sports = models.CharField(max_length=60, null=True)
    amenities = models.TextField(max_length=60, null=True)
    amount = models.IntegerField( null=True)

class resource_tbl(models.Model):
    turf_id = models.ForeignKey(turftbl, on_delete=models.CASCADE, null=True)
    res_name = models.CharField(max_length=10, null=True)
    res_number = models.IntegerField(null=True)


class usertbl(models.Model):
    fname = models.CharField(max_length=20, null=True)
    mname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, null=True)
    district = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=7, null=True)
    dob = models.DateField(null=True)
    phoneno = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    username = models.CharField(max_length=10, null=True)
    password = models.CharField(max_length=10, null=True)

class bookingtbl(models.Model):
    user_id = models.ForeignKey(usertbl,on_delete=models.CASCADE,null=True)
    fname = models.CharField(max_length=20, null=True)
    tname = models.CharField(max_length=20,null=True)
    loc = models.CharField(max_length=15, null=True)
    timing = models.CharField(max_length=6, null=True)
    sports = models.CharField(max_length=6, null=True)
    bookdate = models.DateField(null=True)
    getin = models.TimeField(null=True)
    getout = models.TimeField(null=True)
    items = models.CharField(max_length=7, null=True)
    totalamt = models.IntegerField(null=True)


class reviewrating_tbl(models.Model):
    user_id = models.ForeignKey(usertbl, on_delete=models.CASCADE, null=True)
    review = models.CharField(max_length=15, null=True)

class turfreview_tbl(models.Model):
    user_id = models.ForeignKey(usertbl, on_delete=models.CASCADE, null=True)
    turf_id = models.ForeignKey(turftbl, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(null=True)
    review = models.CharField(max_length=15, null=True)


