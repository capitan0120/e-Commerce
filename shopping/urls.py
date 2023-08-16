from django.urls import path
from django.contrib.auth import views
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/<slug:val>', CategoryView.as_view(), name='category'),
    path('category-title/<val>', CategoryTitle.as_view(), name='category-title'),
    path('product-detail/<int:pk>', ProductDetail.as_view(), name='product-detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('address/', address, name='address'),
    path('update-address/<int:pk>', UpdateAddress.as_view(), name='update-address'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('cart/', show_cart, name='show-cart'),
    path('checkout/', show_cart, name='checkout'),
    path('pluscart/', plus_cart),
    path('minuscart/', minus_cart),
    path('removecart/', remove_cart),

    #login authentication
    path('registration/', CostumerRegistrationView.as_view(), name='costumer-registration'),
    path('accounts/login/', views.LoginView.as_view(template_name='shopping/login.html', authentication_form=LoginForm), name='login'),
    path('password-reset/', views.PasswordResetView.as_view(template_name='shopping/password-reset.html', form_class=MyPasswordResetForm),
         name='password-reset'),
    path('password-change/', views.PasswordChangeView.as_view(template_name='shopping/password-change.html', form_class=MyPasswordChangeForm),
             name='password-change'),
    path('password-change-done/', views.PasswordChangeDoneView.as_view(template_name='shopping/password-change-done.html'),
             name='password-change-done'),
]
