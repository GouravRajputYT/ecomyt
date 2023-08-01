from django.urls import path
from accounts.views import *
# from products.views import 



urlpatterns = [
    path('login/', login_page, name = "login" ),
    path('registration/', login1_page, name = "registration" ),
    path('activate/<email_token>/', activate_email, name = "activate_email" ),
    path('add-to-cart/<uid>/', add_to_cart, name = "add_to_cart"),
    path('cart/', cart, name = "cart"),
    path('remove-cart/<cart_item_uid>/', remove_cart, name = "remove_cart"),
]