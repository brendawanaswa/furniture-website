from django.urls import path
from . import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views  


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    
    path('login/', auth_views.LoginView.as_view(template_name='products/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),

    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/', lambda r: render(r, 'products/checkout_success.html'), name='checkout_success'),

    path('orders/', views.order_history, name='order_history'),

    path('signup/', views.signup, name='signup'),

    # webhooks
    path('webhooks/paystack/', views.paystack_webhook, name='paystack_callback'),
    path('webhooks/stripe/', views.stripe_webhook, name='stripe_webhook'),
]