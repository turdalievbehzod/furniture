from django.urls import path
from products.views import (
    products_list_view,
    product_detail_view,
    cart_view,
    checkout_view,
    wishlist_view,
)

app_name = 'products'

urlpatterns = [
    path('', products_list_view, name='list'),
    path('detail/', product_detail_view, name='detail'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('wishlist/', wishlist_view, name='wishlist'),
]
