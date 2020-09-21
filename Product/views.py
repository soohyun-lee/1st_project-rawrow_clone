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

#카테고리 별 상품 리스트
# class CategoryProducts(View):
#     def get(self, request):
#         category_product = Products.objects.select_related('sub_category').get(id=)
#         n = category_product.sub_category.id
#         pr =Products.objects.filter(sub_category.id = n)
#         return JsonResponse({'data': n}, status=200)

# #각 카테고리별 리스트
# class CategoryProductList(View):
# # #카테고리 전체 상품으로 해야하는데 서브 카테고리를 폴인키로 연결해버림,, 
#     def get(self, request):
#         category_all = Category.objects.all()
#         try:
#             category_products_list = Products.objects.select_related('sub_category').get(id=4)
#             current_category = get_object_or_404(Category, pk=product_id)
#             if category_slug:
#                 category_products_list [{
#                     'thumbnail_image' : products.thumbnail,
#                     'hover_image'     : products.hover_image,
#                     'price'           : products.price,
#                     'sale_price'      : products.sale_price,
#                     'sub_text'        : products.sub_text
#                 }for products in current_category]
#             return JsonResponse({'reuslt':'category_products_list'}, status=200)
#         except:
#             return JsonResponse({'message':'KEY_ERROR'}, status = 400) 


#         # current_category = get_object_or_404(Category, pk=product_id)
#         # categoryproduct = Products.objects.filter(id = category_id).values(
#         #     'thumbnail', 'name', 'price', 'sale_price',
#         #     )
#         # return JsonResponse({'reuslt':'categoryproduct'}, status=200)

        
#         # # current_category = get_object_or_404(Category, pk=product_id)
        # # products = Products.objects.filter(available_display = True)

        # # 

        # products_list [{
        #     'thumbnail_image' : products.thumbnail,
        #     'hover_image'     : products.hover_image,
        #     'price'           : products.price,
        #     'sub_text'        : products.sub_text
        # }for products in current_category]

        # return JsonResponse({'reuslt':'products_list'}, status=200)

# #상세 페이지
class ProductDetailView(View):
    def get(self, request, product_id):
        #왜 자꾸 related product id 만 나오는 것이야,,,,,, 
        try:
            #detail
            pd_products = Products.objects.get(id=product_id)
            image = detail_products.detailimage_set.all()
            #product_group
            th_id = pd_products.product_group.id
            ths = Products.objects.filter(product_group_id = th_id)
            
            test =[]
            for i in ths:
                test.append(i.thumbnail)
            
            product_list = []
            product_list.append({
                'name' : detail_products.name,
                # 'Detail/Image'
                'price' : detail_products.price,
                'sale_price' :detail_products.sale_price,
                'point' : detail_products.point,
                'info' : detail_products.info,
                'notice' :detail_products.notice,
                'test' : test
            })

            return JsonResponse({"mice_list": list(product_list)}, status = 200) 
         
        except ValueError:
            return JsonResponse({"message": 'INVALID_CATEGORY'}, status = 400)





# # 상세 원본(이건 제대로 들어옴)
# class ProductDetailView(View):
#     def get(self, request, product_id):
#         #왜 자꾸 related product id 만 나오는 것이야,,,,,, 
#         product = []
#         # Detail = Products.objects.select_related('DetailImage').get(name=277)
        
#         product = Products.objects.filter(id = product_id).values(
#             'name', 'thumbnail','price', 'sale_price', 'point','info', 'notice'
#              )
#         return JsonResponse({'product':list(product)},status = 200)

#         product = [{
#             'name' : Products.name,
#             # 'detail_image' : detail_image,
#             'related_product' : category_products_list.name
#         }]

#         return JsonResponse({'product':product},status = 200)



