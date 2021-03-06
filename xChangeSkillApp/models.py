from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import datetime

class User(AbstractUser):
    email=models.EmailField(('email'), unique=True)
    mid_name = models.CharField(max_length=20)
    dob = models.DateField(default=datetime.date.today)
    phone = models.IntegerField(null=True)
    gender = models.CharField(max_length=1)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Address(models.Model):
    street_address = models.CharField(max_length=50)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def create(self, street_address, country, state, city, zip_code, user):
        self.street_address = street_address
        self.country = country
        self.state = state
        self.city = city
        self.zip_code = zip_code
        self.user = user
        return self

class SkillList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)

class SkillWishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)