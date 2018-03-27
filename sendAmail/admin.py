from django.contrib import admin
from sendAmail.models import EmailModel,UserProfile

admin.site.register(EmailModel)
admin.site.register(UserProfile)

# Register your models here.
