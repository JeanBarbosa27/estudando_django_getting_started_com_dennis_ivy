from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

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

    path('', views.dashboard, name='dashboard'),
    path('user-page/', views.user_page, name='user_page'),
    path('profile/', views.profile_page, name='profile'),
    path('products/', views.products, name='products'),

    path('customer/<str:customer_id>', views.customers, name='customer'),
    path('create-order/<str:customer_id>', views.create_order, name='create_order'),
    path('update-order/<str:order_id>', views.update_order, name='update_order'),
    path('delete-order/<str:order_id>', views.delete_order, name='delete_order'),
]
