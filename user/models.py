from django.db import models

class User(models.Model):
    userid      = models.CharField(max_length = 50)
    password    = models.CharField(max_length = 100)
    user_name   = models.CharField(max_length = 50)
    address     = models.CharField(max_length = 100)
    telephone   = models.CharField(max_length = 20)
    phonenumber = models.CharField(max_length = 20)
    email       = models.CharField(max_length = 100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'


