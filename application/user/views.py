from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.models import User
from user.forms import LoginForm
from django.contrib import messages

class Login(View):

    def get(self, request):
        login_form = LoginForm()
        return render(
            request,
            'user/login.html',
            {
                'login_form': login_form,
            }
        )

    def post(self, request):
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.info(request, 'Logged in successfully.', extra_tags='ok')
                return redirect('dashboard')
            else:
                login_form = LoginForm(request.POST)
                messages.info(request, 'Account has been disabled!', extra_tags='ban-circle')
                return render(request, 'user/login.html', {
                    'login_form': login_form,
                })
        else:
            login_form = LoginForm(request.POST)
            messages.info(request, 'The username and password were incorrect.', extra_tags='ban-circle')
            return render(request, 'user/login.html', {
                'login_form': login_form,
            })

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('user_login')
