from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('blog/',views.blog,name="blog"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('myaccount/',views.myaccount,name="myaccount"),
    path('signup/',views.signup,name="signup"),
    path('check_otp/',views.check_otp,name="check_otp"),
    path('product_details/',views.product_details,name="product_details"),
    path('myorder/',views.myorder,name="myorder"),

    path('product_details/<int:pk>',views.product_details,name="product_details"),
    path('shoping_cart/',views.shoping_cart,name="shoping_cart"),
    
    path('shop/',views.shop,name="shop"),
    path('shop1/<int:pk>',views.shop1,name="shop1"),
    path('shop2/<int:pk>',views.shop2,name="shop2"),
    

    path('change_password/',views.change_password,name="change_password"),
    path('forgot_password/',views.forgot_password,name="forgot_password"),
    path('chk_otp_forgot_password/',views.chk_otp_forgot_password,name="chk_otp_forgot_password"),
    path('get_reset_password/',views.get_reset_password,name="get_reset_password"),

    path('add_to_wishlist/<int:pk>',views.add_to_wishlist,name="add_to_wishlist"),
    path('mywishlist/',views.mywishlist,name="mywishlist"),
    path('remove_from_wishlist/<int:pk>',views.remove_from_wishlist,name="remove_from_wishlist"),
    path('update_qty_in_cart/<int:pk>',views.update_qty_in_cart,name="update_qty_in_cart"),


    
    path('add_to_cart/<int:pk>',views.add_to_cart,name="add_to_cart"),
    path('mycart/',views.mycart,name="mycart"),
    path('remove_from_cart/<int:pk>',views.remove_from_cart,name="remove_from_cart"),

    
    path('checkout/',views.checkout,name="checkout"),
    path('pay/',views.pay,name="pay"),
    path('invoice/',views.invoice,name="invoice"),

    
 ]