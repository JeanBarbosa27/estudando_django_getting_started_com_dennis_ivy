from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from accounts.forms import CreateUserForm
from accounts.decorators import unauthenticated_user

@method_decorator(unauthenticated_user, name='dispatch')
class RegisterPageView(View):
    def get(self, request):
        form = CreateUserForm()

        return render(request, 'pages/register.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']

            message = f"Account was created for {username}."
            messages.success(request, message)

            return redirect('login')
