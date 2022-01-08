from django.urls import path

from . import views
app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /product/5/
    path('<int:product_id>/', views.detail, name='detail'),
    # ex: /product/5/cart/
    path('<int:product_id>/cart/', views.cart, name='cart'),
    # ex: /product/5/cart/checkout/    
    path('<int:product_id>/cart/checkout', views.checkout, name='checkout'),
    #product/cart/
    path('<int:product_id>/cart/checkout/confirmation', views.confirmation, name='confirmation'),

    # path('cart/', views.cart, name='cart'),
    #product/checkout/
    # path('<int:pk>/', views.checkout, name='checkout'),
    #product/confirmation/
    # path('confirmation/', views.confirmation, name='confirmation'),
    #product/product-single/1
    # path('product-single/<int:my_id>/', views.productsingle, name='product-single')

]
