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
    
 ]