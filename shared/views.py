from django.http import Http404
from django.shortcuts import redirect, render


LEGACY_HTML_TEMPLATE_MAP = {
    'home': 'shared/home.html',
    'about-us': 'shared/about-us.html',
    'contact': 'shared/contact.html',
    '404': 'shared/404.html',
    'blogs-list': 'blogs/blogs-list.html',
    'blog-detail': 'blogs/blog-detail.html',
    'products-list': 'products/products-list.html',
    'product-detail': 'products/product-detail.html',
    'cart': 'products/cart.html',
    'checkout': 'products/checkout.html',
    'wishlist': 'products/wishlist.html',
    'login': 'users/login.html',
    'register': 'users/register.html',
    'account': 'users/account.html',
    'reset-password': 'users/reset-password.html',
}


def home_page_view(request):
    return render(request, 'shared/home.html')


def contact_page_view(request):
    return render(request, 'shared/contact.html')


def about_page_view(request):
    return render(request, 'shared/about-us.html')


def not_found_page_view(request):
    return render(request, 'shared/404.html')


def legacy_html_page_view(request, page):
    template_name = LEGACY_HTML_TEMPLATE_MAP.get(page)
    if not template_name:
        raise Http404('Page not found')
    return render(request, template_name)


def legacy_html_redirect_view(request, page):
    if page in LEGACY_HTML_TEMPLATE_MAP:
        return redirect(f'/{page}.html')
    raise Http404('Page not found')
