from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import *


urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),

    path(
        'reset-password',
        auth_views.PasswordResetView.as_view(
            template_name='pages/reset_password.html'
        ),
        name="reset_password"
    ),
    path(
        'reset-password-sent',
        auth_views.PasswordResetDoneView.as_view(
            template_name='pages/reset_password_sent.html'
        ),
        name="password_reset_done"
    ),
    path(
        'reset-password-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='pages/reset_password_confirm.html'
        ),
        name="password_reset_confirm"
    ),
    path(
        'reset-password-complete',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='pages/reset_password_complete.html'
        ),
        name="password_reset_complete"
    ),

    path('', DashboardView.as_view(), name='dashboard'),
    path('user-page/', UserPageView.as_view(), name='user_page'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('products/', ProductsView.as_view(), name='products'),

    path('customer/<str:customer_id>', CustomersView.as_view(), name='customer'),
    path('create-order/<str:customer_id>', CreateOrderView.as_view(), name='create_order'),
    path('update-order/<str:order_id>', UpdateOrderView.as_view(), name='update_order'),
    path('delete-order/<str:order_id>', DeleteOrderView.as_view(), name='delete_order'),
]
