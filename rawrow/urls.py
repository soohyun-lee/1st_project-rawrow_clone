from django.urls import path, include

urlpatterns = [

    path('', include('user.urls')),
    path('products', include('Product.urls')),
    path('cart', include('cart.urls')),

]
