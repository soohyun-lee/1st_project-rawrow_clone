from django.db import models

class MainCategory(models.Model):
	name  = models.CharField(max_length=45)

	class Meta:
	    db_table = 'main_categories'

class Category(models.Model):
	name          = models.CharField(max_length = 45)
	main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

	class Meta:
	    db_table = 'categories'

class SubCategory(models.Model):
	name          = models.CharField(max_length = 45)
	category      = models.ForeignKey(Category, on_delete =models.CASCADE)

	class Meta:
	    db_table = 'sub_categories'


class ProductGroup(models.Model):
	name  = models.CharField(max_length = 45, null=True)
	subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)


	class Meta:
	    db_table = 'product_group'

class Products(models.Model):	
	name          = models.CharField(max_length = 45)
	price 		    = models.IntegerField(default = 0)	
	point		      = models.IntegerField(default = 0)
	thumbnail     = models.CharField(max_length = 100)
	description   = models.TextField()
	info		      = models.TextField()
	notice        = models.TextField()
	sale_price	  = models.IntegerField(null=True)
	sub_category  = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	hover_image   = models.CharField(max_length=100, null = True)
	product_group = models.ForeignKey(ProductGroup, on_delete = models.CASCADE)
	sub_text	    = models.CharField(max_length=45, null=True)

	class Meta:
	    db_table = 'products'


class DetailImage(models.Model):
        name         = models.ForeignKey(Products, on_delete=models.CASCADE)
        detailImage  = models.TextField()

        class Meta:
            db_table = 'detailImage'


class ProductCategory(models.Model):
	product    = models.ManyToManyField(Products)
	category   = models.ManyToManyField(Category)
	
	class Meta:
	    db_table = 'product_categories'


class ProductRelated(models.Model):
	product          = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product')
	related_product  = models.ForeignKey(Products, on_delete=models.CASCADE, related_name ='related_product')

	class Meta:
	    db_table = 'product_related'

