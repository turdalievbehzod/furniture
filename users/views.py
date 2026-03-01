import threading

from django.shortcuts import redirect, render
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail

from users.forms import CustomUserCreationForm
from django.contrib import messages
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from users.utils import email_verification_token
from django.contrib.auth import get_user_model, login

User = get_user_model()

def login_view(request):
    return render(request, 'users/login.html')


def register_view(request):
    if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.is_active = False 
                user.save()
                
                # send verificaton link
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = email_verification_token.make_token(user)
                domain = get_current_site(request).domain
                link = f'http://{domain}/verify/{uid}/{token}/'
                
                thread = threading.Thread(target=send_mail, kwargs={
                    'subject':'Verify your email',
                    'message':f'Click to verify your account: {link}',
                    'from_email':'noreply@yourapp.com',
                    'recipient_list':[user.email],
                })
                thread.start()

                text = 'We sent a confirmation link to your email, please verify it'
                messages.success(request, text)
                return redirect('users:register')
            else:
                errors = []
                for field, field_errors in form.errors.items():
                    for error in field_errors:
                        errors.append(f"{field}: {error}")

                error_text = " | ".join(errors)
                messages.error(request, error_text)
                return render(request, 'shared/contact.html')
    else:
        return render(request, 'users/register.html')

def verify_email_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, User.DoesNotExist()):
        user = None
        
    if user and email_verification_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('shared:home')
    else:
        messages.error(request, "Something went wrong, please try again later")
        return render(request, 'users:login.html')

def account_view(request):
    return render(request, 'users/account.html')


def reset_password_view(request):
    return render(request, 'users/reset-password.html')
