from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField( max_length=12,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    # subject = models.CharField(max_length=50,null=True,blank=True)
    date = models.DateField()

    def __str__(self) :
        return self.email

class Enquiry(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField( max_length=12,null=True,blank=True)
    description = models.TextField()
    date = models.DateField()

    def __str__(self) :
        return self.email

class Dietenquiry(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField( max_length=12,null=True,blank=True)
    age = models.IntegerField()
    height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    reason = models.TextField()
    goal = models.TextField()

    def __str__(self) :
        return self.email

class Banner(models.Model):
    img = models.ImageField(upload_to='Banner/')