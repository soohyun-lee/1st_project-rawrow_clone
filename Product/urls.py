from django.urls import path
from .views      import AllProducts,ProductDetailView,CategoryProductList, SearchProducts

urlpatterns = [
    path('/products',AllProducts.as_view()),
    path('/list',AllProducts.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/category/list', CategoryProductList.as_view()),
    path('/search', SearchProducts.as_view()),
]
