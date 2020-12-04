from django.db import models
from user.models import User
from Product.models import Products
from datetime import datetime

class Cart(models.Model):	
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	product = models.ForeignKey(Products, on_delete = models.CASCADE)
	quantity = models.IntegerField(default = 1)

	class Meta:
	    db_table = 'cart'
