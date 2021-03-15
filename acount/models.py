from django.db import models

class Userinfo(models.Model):
    user = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    pwd = models.CharField(max_length=32)
    age = models.IntegerField()
    sex = models.IntegerField()

class UserAva(models.Model):
    img_path = models.CharField(max_length=256)
    u = models.OneToOneField('Userinfo',on_delete=models.CASCADE)

class student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    in_date = models.DateField(auto_now_add=True)
    sex = models.IntegerField(
        choices=((1,'男'),(2,'女'))
    )
    cls = models.ForeignKey('cls',on_delete=models.DO_NOTHING)

class cls(models.Model):
    title = models.CharField(max_length=32)
    t = models.ManyToManyField('teacher')

class teacher(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    sex = models.IntegerField(
        choices=((1,'男'),(2,'女'))
    )