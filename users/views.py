from django.shortcuts import render


def login_view(request):
    return render(request, 'users/login.html')


def register_view(request):
    return render(request, 'users/register.html')


def account_view(request):
    return render(request, 'users/account.html')


def reset_password_view(request):
    return render(request, 'users/reset-password.html')
