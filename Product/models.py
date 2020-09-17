from django.db import models
class Main_category(models.Model):
	main_category = models.CharField(max_length=45)


class Category(models.Model):
	category 	  = models.CharField(max_length = 45)
	main_category = models.ForeignKey(Main_category, on_delete=models.CASCADE)

class Sub_category(models.Model):
	sub_category  = models.CharField(max_length = 45)
	category 	  = models.ForeignKey(Category, on_delete =models.CASCADE)


class Product_group(models.Model):
	product_group_name  = models.CharField(max_length = 45, null=True)

class Products(models.Model):	
	product_name  	 = models.CharField(max_length = 45)
	price 		  	 = models.IntegerField(default = 0)	
	point		 	 = models.IntegerField(default = 0)
	thumbnail        = models.CharField(max_length = 100)
	description      = models.TextField()
	info		     = models.TextField()
	notice           = models.TextField()
	sale_price	     = models.IntegerField(null=True)
	sub_category     = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
	hover_image      = models.BooleanField(default = False, null = True)
	product_group    = models.ForeignKey(Product_group, on_delete = models.CASCADE)
	detail_image_url = models.TextField()
	# detail_image_url에 List를 넣으려고 하는데, 어떤 Field를 써야하는지 모르겠습니다
	sub_text	  	 = models.CharField(max_length=45, null=True)


class Product_category(models.Model):
	product    = models.ManyToManyField(Products)
	category   = models.ManyToManyField(Category)


class Product_related(models.Model):
	product          = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product')
	related_product  = models.ForeignKey(Products, on_delete=models.CASCADE, related_name ='related_product')



