from django.urls import path
from users.views import login_view, register_view, account_view, reset_password_view, verify_email_view

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('account/', account_view, name='account'),
    path('reset-password/', reset_password_view, name='reset-password'), 
    path('verify-email/', verify_email_view, name='verify-email'),
]
