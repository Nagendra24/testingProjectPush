from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class EmailModel(models.Model):
    to_mail = models.EmailField(max_length=50)
    from_mail = models.EmailField(max_length=50)
    message = models.CharField(max_length=250)

    class Meta:
        db_table = 'email_table'
    def __str__(self):
        return self.to_mail

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)

    class Meta:
        db_table = 'userprofile'
    def __str__(self):
        return self.city


# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile,sender = User)

# class RegistrationModel(models.Model):
#     name = models.CharField(max_length=20)
#     email = models.EmailField(max_length=50)
#     phone_number = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'registration_table'

# Create your models here.
