from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class users_db(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Phone number must be entered in the format: '+999999999'. upto 10 digits.")
    phone_num = models.CharField(validators=[phone_regex], max_length=10, blank=True) # Validators should be a list
    gender = models.CharField(max_length=15)
    dob = models.DateField(auto_now=False,default=False)
    profilepic = models.FileField(upload_to = 'users/pc/', default='default.png')

class Todos(models.Model):
    todo_name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)