from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.decorators import allowed_users
from accounts.forms import ProfileForm

@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['customer']), name='dispatch')
class ProfilePageView(View):

    def get(self, request):
        '''
        TODO: ver uma forma de pegar o request no contructor, pra não precisar
            repetir a variável em ambos os métodos
        '''
        customer = request.user.customer
        form = ProfileForm(instance=customer)

        return render(request, 'pages/profile.html', {'form': form})

    def post(self, request):
        customer = request.user.customer
        form = ProfileForm(instance=customer)

        form = ProfileForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

        return render(request, 'pages/profile.html', {'form': form})
