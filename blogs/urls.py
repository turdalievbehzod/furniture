from django.urls import path, re_path

from blogs.views import blogs_list_view, blog_detail_view
from shared.views import legacy_html_redirect_view

app_name = 'blogs'

urlpatterns = [
    path('', blogs_list_view, name='list'),
    path('blogs-list.html', blogs_list_view, name='list-html'),
    path('detail/', blog_detail_view, name='detail'),
    path('blog-detail.html', blog_detail_view, name='detail-html'),
    path('<int:pk>/', blog_detail_view, name='detail-by-id'),
    re_path(r'^(?P<page>[\w-]+)\.html$', legacy_html_redirect_view),
]
