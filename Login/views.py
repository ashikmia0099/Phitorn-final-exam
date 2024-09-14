from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

# for email import data

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def RegisterPage(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()


            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            confirm_link = f"http://127.0.0.1:8000/Login-Logout/active/{uid}/{token}"
            email_subject ="Confirm Your Email"
            email_body = render_to_string('confirm_email.html',{'confirm_link': confirm_link})
            
            
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            messages.success(request, 'Check your email address for confirmation.')
            return redirect('RegisterPage')
    
    else:
        form = RegisterForm()
            
    
    return render(request, 'register.html', {'form': form})


def activate(request, uid64, token):
    
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)

    except(User.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        
        user.is_active = True
        user.save()
        return redirect('LoginPage')
    
    else:
        return redirect('RegisterPage')


def LoginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                login(request, user)
                messages.success(request, f'Welcome {user.first_name} {user.last_name}!')
                return redirect('homepage')
                
            else:
                messages.error(request, 'Login information is incorrect.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})



@login_required
def LogoutView(request):
    user = request.user
    logout(request)
    messages.success(request, f'{user.first_name} {user.last_name} is successfully logged out.')
    return redirect('LoginPage')
 