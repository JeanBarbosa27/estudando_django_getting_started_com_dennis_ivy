from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login

from accounts.decorators import unauthenticated_user
from accounts.forms import CreateUserForm

@method_decorator(unauthenticated_user, name='dispatch')
class LoginPageView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'pages/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or password is incorrect!')
