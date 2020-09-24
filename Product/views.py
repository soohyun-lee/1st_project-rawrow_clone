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

class AllProducts(View):
    def get(self, request):
        order_method = int(request.GET.get('sort_method', None))
        print(order_method)
        
        if order_method == 0:
            product_all  = Products.objects.order_by('?')
        elif order_method == 1:
            product_all  = Products.objects.order_by(min('sale_price','price'))
        elif order_method == 2:
            product_all  = Products.objects.order_by('-price')

        new_ = []
        for product in product_all:        
            new_.append({
                'sub_category_id'    : product.id,
                'id'                 : product.id,
                'name'               : product.name,
                'price'              : product.price,
                'thumbnail'          : product.thumbnail,
                'hover_image'        : product.hover_image,
                'sale_price'         : product.sale_price,
            })

        return JsonResponse({'data': new_}, status=200)



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

#상세 페이지
class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            detail_products = Products.objects.get(id=product_id)

            #detail
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
            
            #related_product:
            related_id = detail_products.product.all()

            product_list = []
            product_list.append({
                'name'            : detail_products.name,
                'price'           : detail_products.price,
                'sale_price'      : detail_products.sale_price,
                'point'           : detail_products.point,
                'info'            : detail_products.info,
                'notice'          : detail_products.notice,
                'thumbnail_group' : new_list,
                'detailimage'     : detail_list,

                'related_group'   : [{
                    'related_id'            : i.related_product.id ,
                    'related_name'          : i.related_product.name,
                    'related_thumbnail'     : i.related_product.thumbnail,
                    'related_price'         : i.related_product.price,
                    'related_sale_price'    : i.related_product.sale_price,
                }for i in related_id]
            })

            return JsonResponse({"data": list(product_list)}, status = 200) 
         
        except ValueError:
            return JsonResponse({"message": 'INVALID_PRODUCT'}, status = 400)
