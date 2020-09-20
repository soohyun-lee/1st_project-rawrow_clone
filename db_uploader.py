import os
import django
import csv
import sys
# from starbucks import starbucks_defaults
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rawrow.settings")
django.setup()
from Product.models import *

CSV_PATH_PRODUCTS = 'csv_files/done/clear_all_product.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)

    # PRODUCT_GROUP DUMP하는 코드
    # for row in data_reader:
    #     if row[0]:
    #         category = row[0]

    #     if row[1]:
    #         subCategory = row[1]

    #     if row[2]:
    #         product_group = row[2]
    #         categories = Category.objects.get(name = category)
    #         subCategories = SubCategory.objects.get(name = subCategory, category=categories)
    #         ProductGroup.objects.create(name = product_group, sub_category = subCategories)

    # PRODUCT DUMP 하는 코드
    # for row in data_reader:
    #     p_name = row[6]
    #     p_price = row[7]
    #     p_point = row[9]
    #     p_thumbnail = row[3]
    #     p_description = row[11]
    #     p_info = row[12]
    #     p_notice = row[13]
    #     p_sale_price = row[8]
    #     if p_sale_price == '':
    #         p_sale_price = 0
    #     p_hover_image = row[4]
    #     p_sub_text = row[10]
    #     if row[0]:
    #         p_category = row[0]
    #     if row[1]:
    #         p_subCategory = row[1]

    #     if row[2]:
    #         p_product_group = row[2]
    #         categories = Category.objects.get(name=p_category)
    #         subcategories = SubCategory.objects.get(name=p_subCategory, category=categories)
    #         product_groups= ProductGroup.objects.get(name =p_product_group, sub_category=subcategories)
    #     Products.objects.create(name=p_name, price=p_price, point=p_point, thumbnail=p_thumbnail, description=p_description, info=p_info,notice=p_notice,sale_price=p_sale_price, sub_category = subcategories, product_group = product_groups, sub_text=p_sub_text)
