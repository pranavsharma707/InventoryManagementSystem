from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    staff=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=20,null=True)
    profile=models.ImageField(default='avatar.jpg',upload_to='Profile_Images')
    #in media folder and also MEDIA_URL and MEDIA_ROOT we have to configure settings.py
    #after settings media folder by default created
    #this avtar.jpg should be availa ble in media other when you click

    def __str__(self):
        return f'{self.staff.username}-Profile'
 
