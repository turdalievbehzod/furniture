from django.urls import path, re_path

from shared.views import legacy_html_redirect_view
from users.views import login_view, register_view, account_view, reset_password_view

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('login.html', login_view, name='login-html'),
    path('register/', register_view, name='register'),
    path('register.html', register_view, name='register-html'),
    path('account/', account_view, name='account'),
    path('account.html', account_view, name='account-html'),
    path('reset-password/', reset_password_view, name='reset-password'),
    path('reset-password.html', reset_password_view, name='reset-password-html'),
    re_path(r'^(?P<page>[\w-]+)\.html$', legacy_html_redirect_view),
]
