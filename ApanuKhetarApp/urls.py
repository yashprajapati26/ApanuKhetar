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
    path('shop_details/',views.shop_details,name="shop_details"),
    path('change_password/',views.change_password,name="change_password"),
    path('forgot_password/',views.forgot_password,name="forgot_password"),
    path('chk_otp_forgot_password/',views.chk_otp_forgot_password,name="chk_otp_forgot_password"),

    path('get_reset_password/',views.get_reset_password,name="get_reset_password"),

    
 ]