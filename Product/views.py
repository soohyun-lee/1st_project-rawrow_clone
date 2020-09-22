from django.shortcuts      import render
from django.views          import View
from django.http           import JsonResponse
from django.db             import models
from .models               import (
    MainCategory,
    Category,
    SubCategory,
    ProductGroup,
    Products,
    DetailImage,
    ProductCategory,
    ProductRelated,
)



#product 전체 리스트 #한 페이지에 몇개 나오게 할 지
class AllProducts(View):
    def get(self, request):
        allproduct = list(Products.objects.values('thumbnail', 'name','price','sale_price'))

        return JsonResponse({'data': allproduct}, status=200)


#상세 페이지
class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            #detail
            detail_products = Products.objects.get(id=product_id)
            image = detail_products.detailimage_set.all()
            detail_list = []
            for n in image:
              detail_list.append(n.detailImage)
            #product_group
            group_id = detail_products.product_group.id
            group_ = Products.objects.filter(product_group_id = group_id)
            
            new_list =[]
            for i in group_:
                new_list.append(i.thumbnail)
            
            product_list = []
            product_list.append({
                'name'            : detail_products.name,
                'price'           : detail_products.price,
                'sale_price'      : detail_products.sale_price,
                'point'           : detail_products.point,
                'info'            : detail_products.info,
                'notice'          : detail_products.notice,
                'thumbnail_group' : new_list
                'detailimage'     : detail_list
            })

            return JsonResponse({"data": list(product_list)}, status = 200) 
         
        except ValueError:
            return JsonResponse({"message": 'INVALID_PRODUCT'}, status = 400)


