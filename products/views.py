from django.shortcuts import render


def products_list_view(request):
    return render(request, 'products/products-list.html')


def product_detail_view(request):
    return render(request, 'products/product-detail.html')


def cart_view(request):
    return render(request, 'products/cart.html')


def checkout_view(request):
    return render(request, 'products/checkout.html')


def wishlist_view(request):
    return render(request, 'products/wishlist.html')
