from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('user-page/', views.user_page, name='user_page'),
    path('products/', views.products, name='products'),
    path('customer/<str:customer_id>', views.customers, name='customer'),
    path('create-order/<str:customer_id>', views.create_order, name='create_order'),
    path('update-order/<str:order_id>', views.update_order, name='update_order'),
    path('delete-order/<str:order_id>', views.delete_order, name='delete_order'),
]
