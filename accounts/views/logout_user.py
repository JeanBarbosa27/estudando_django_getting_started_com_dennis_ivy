from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout

from accounts.decorators import unauthenticated_user


class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
