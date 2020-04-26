from django.shortcuts import render, redirect 
from django.contrib.auth import (
    authenticate, 
    get_user_model,
    login,
    logout,
) 
from django.contrib import messages
from .forms import UserLoginForm, UserRegisterForm
# Create your views here.
def login_view(request):
    title = 'Login'
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    context = {
        'form' : form,
        'title' : title,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,  password=password)
        login(request, user) 
        if next:
            return redirect(next) 
        return redirect('/') 
    return render(request, 'Loginform.htm', context )

def logout_view(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

def register_view(request):
    form = UserRegisterForm(request.POST or None )

    if form.is_valid():
        
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
         
        return redirect('login')

    return render(request, 'Registerform.htm', {'form':form})