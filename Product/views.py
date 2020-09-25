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

#search 기능
class SearchProducts(View):
    def get(self, request):
        search_key = request.GET.get("keyword") # 검색어 가져오기
        product_list = Products.objects.all()
        if search_key and search_key != "": # 만약 검색어가 존재하면
            search_product = product_list.filter(name__icontains =search_key)
            product_info = [{
            'category'           : product.sub_category.category.name,
            'id'                 : product.id,
            'thumbnail'          : product.thumbnail,
            'name'               : product.name,
            'price'              : product.price,
            'sale_price'         : product.sale_price
            } for product in search_product]
        
            return JsonResponse({'data':product_info}, status=200)
        return JsonResponse({'data':None}, status=200)

# 전체 상품 리스트
class AllProducts(View):
    def get(self, request):
        try:
            product_info = [{
            'id'                 : product.id,
            'name'               : product.name,
            'price'              : product.price,
            'thumbnail'          : product.thumbnail,
            'hover_image'        : product.hover_image,
            'sale_price'         : product.sale_price,
            'sub_text'           : product.sub_text,
            } for product in product_all]
            return JsonResponse({'data': product_info}, status=200)
        except ValueError:
            return JsonResponse({"message": 'INVALID_CATEGORY'}, status = 400)

# # #각 카테고리별 리스트 
class CategoryProductList(View):
    def get(self, request):
        category_id = request.GET.get("category", None)
        subcategory_id = request.GET.get("subcategory", None)

        if subcategory_id == None:
            subcategories = SubCategory.objects.filter(category_id = category_id).prefetch_related("products_set")
        else:
            subcategories = SubCategory.objects.filter(id = subcategory_id).prefetch_related("products_set")        
        new_ = []
        for i in subcategories:
            for product in Products.objects.filter(sub_category_id = i.id ):        
                new_.append({
                    'sub_category_id'    : i.id,
                    'id'                 : product.id,
                    'name'               : product.name,
                    'price'              : product.price,
                    'thumbnail'          : product.thumbnail,
                    'hover_image'        : product.hover_image,
                    'sale_price'         : product.sale_price,
                })

        return JsonResponse({'data': new_}, status=200)

# #상세 페이지 뷰
class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Products.objects.get(id=product_id)

            #detailimage
            image = product.detailimage_set.all()
            detail_list =[]
            for i in image:
                detail_list.append(i.detailImage)

            # product_group_image
            product_group = product.product_group.id
            group_p = Products.objects.filter(product_group_id = product_group)
            group_list =[]
            for i in group_p:
                group_list.append(i.thumbnail)

            product_info = [{
                'detailimage'     : detail_list,
                'name'            : product.name,
                'price'           : product.price,
                'sale_price'      : product.sale_price,
                'point'           : product.point,
                'sub_text'        : product.sub_text,
                'group_thumbnail' : group_list,
            }]
            return JsonResponse({"data": list(product_info)}, status = 200) 
        except ValueError:
            return JsonResponse({"message": 'INVALID_CATEGORY'}, status = 400)
=======
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
