from django.urls import path
from .views      import AllProducts, ProductDetailView
# AllProducts, ProductDetailView, 
urlpatterns = [
    path('product',AllProducts.as_view()),
    path('detail/<int:product_id>', ProductDetailView.as_view()),

]
