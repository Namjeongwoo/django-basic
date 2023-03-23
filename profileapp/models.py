from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # on_delete : User 객체가 사라질 때 profile 또한 사라지도록 설정

    image = models.ImageField(upload_to='profile/', null=True)
    # media 하위 경로에 profile/ 설정

    nickname = models.CharField(max_length=20, unique=True, null=True)

    message = models.CharField(max_length=100, null=True)
