from django.urls import path, re_path

from products.views import (
    products_list_view,
    product_detail_view,
    cart_view,
    checkout_view,
    wishlist_view,
)
from shared.views import legacy_html_redirect_view

app_name = 'products'

urlpatterns = [
    path('', products_list_view, name='list'),
    path('products-list.html', products_list_view, name='list-html'),
    path('detail/', product_detail_view, name='detail'),
    path('product-detail.html', product_detail_view, name='detail-html'),
    path('cart/', cart_view, name='cart'),
    path('cart.html', cart_view, name='cart-html'),
    path('checkout/', checkout_view, name='checkout'),
    path('checkout.html', checkout_view, name='checkout-html'),
    path('wishlist/', wishlist_view, name='wishlist'),
    path('wishlist.html', wishlist_view, name='wishlist-html'),
    re_path(r'^(?P<page>[\w-]+)\.html$', legacy_html_redirect_view),
]
