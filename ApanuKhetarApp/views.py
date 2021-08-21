from django.shortcuts import render
from . models import *
from . utils import *
from random import *

# Create your views here.

data = {}
category = Category.objects.all()
sub_category = Sub_Category.objects.all()
products = Product.objects.all()
data['category'] = category
data['sub_category'] = sub_category
data['products'] = products


def index(request):
    print(data['category'])
    return render(request, 'index.html',data)

def contact(request):
    return render(request, 'contact.html',data)

def blog(request):
    return render(request, 'blog.html',data)

def shop_details(request):
    return render(request, 'shop_details.html',data)

def shoping_cart(request):
    return render(request, 'shoping_cart.html',data)

def logout(request):
    del request.session['email']
    del request.session['name']
    return render(request,'index.html',data)

def login(request):
    if request.method == 'POST':
        Email = request.POST['femail']
        Password = request.POST['fpassword',data]
        
        try:
            user = User.objects.get(Email=Email,Password=Password)
            if user.Status == 'Active':
                request.session['name']=user.FirstName
                request.session['email']=user.Email
               
                print(request.session['email'])
                return render(request,'index.html',data)
            else:
                msg="your account is not active"
                global gen_otp
                email_Subject = "OTP For Login Verification From ApanuKhetar"
                gen_otp = randint(1000,9999) 
                print(gen_otp)
                sendmail(email_Subject,'otpVerification_emailTemplate',Email,{'name':user.FirstName,'gen_otp':gen_otp})
                return render(request, 'otp_signup.html',{'gen_otp':gen_otp,'femail':Email},data)
                
        except Exception as e:
            print(e)
            if Email=="" and Password=="":
                msg="please enter all fileds"
                return render(request,'login.html',{'msg1':msg},data)
            else:
                msg="somothing wrong."
                return render(request,'login.html',{'msg1':msg},data)
            
        # return render(request, 'index.html')
    else:
        return render(request, 'login.html',data)

def signup(request):
    if request.method == 'POST':
        global u
        u=User()
        u.FirstName = request.POST['ffname']
        u.LastName = request.POST['flname']
        u.Email = request.POST['femail']
        u.Password = request.POST['fpass']
        ConfirmPassword = request.POST['fcpass']
        try:
            user = User.objects.get(Email=u.Email)
            if user:
                msg="This Email is already register"
                return render(request,'login.html',{'msg':msg},data)
        except:
            if u.FirstName=="" or u.LastName=="" or u.Email=="" or u.Password=="" or ConfirmPassword=="":
                msg="please enter all details!"
                return render(request,'login.html',{'msg':msg},data)
            elif u.Password == ConfirmPassword:
                # User.objects.create(FirstName=u.FirstName, LastName=u.LastName, Email=u.Email, Password=u.Password)
                global gen_otp
                email_Subject = "OTP For SignUp Verification From ApanuKhetar"
                gen_otp = randint(1000,9999) 
                print(gen_otp)
                sendmail(email_Subject,'otpVerification_emailTemplate',u.Email,{'name':u.FirstName,'gen_otp':gen_otp})
                return render(request, 'otp_signup.html',{'gen_otp':gen_otp},data)
            else:
                msg="password & confirm password does not match"
                return render(request,'login.html',{'msg':msg},data)
    
    else:
        return render(request, 'login.html',data)



def check_otp(request):
    if request.method == 'POST':
        votp = request.POST['fotp']
        vgen_otp = request.POST['gen_otp']
        vemail = request.POST['femail']
        print(votp)
        print(vgen_otp)

        UserLogin = User.objects.get(Email=vemail)
        if UserLogin:
            UserLogin.Status="Active"
            UserLogin.save()
            request.session['name']=UserLogin.FirstName
            request.session['email']=UserLogin.Email
            print("--login Sucessfully--")
            return render(request,'index.html',data)

        if votp == vgen_otp:
            user=User.objects.create(FirstName=u.FirstName, LastName=u.LastName, Email=u.Email, Password=u.Password, Status="Active")
            request.session['name']=user.FirstName
            request.session['email']=user.Email

            print(request.session.name)
            print(request.session.email)

            print(user)
            return render(request,'index.html',data)
        else:
            msg="OTP is Wrong. Please Enter Valid OTP."
            return render(request,'otp_signup.html',{'msg':msg,'gen_otp':vgen_otp},data)
    else:
        return render(request,'otp_signup.html',data)

def myaccount(request):
    user = User.objects.get(Email=request.session['email'])
    print(user)
    return render(request,'myaccount.html',{'user':user})

def change_password(request):
    user = User.objects.get(Email=request.session['email'])

    if request.method == 'POST':
        v_old_pass=request.POST['foldpass']
        v_new_pass=request.POST['fnewpass']
        v_confirm_pass = request.POST['fcnewpass']

        if v_old_pass == user.Password:
            if v_old_pass == v_new_pass:
                msg="Please Enter Different Password."
                return render(request,'change_password.html',{'msg':msg},data)
            elif v_new_pass == v_confirm_pass:
                user.Password = v_new_pass
                user.save()
                msg="Password Change Sucessfully."
                return render(request,'myaccount.html',{'user':user,'msg':msg},data)
                
            else:
                msg="New Password And Confirm Password Is Not Matched."
                return render(request,'change_password.html',{'msg':msg},data)
        else:
            msg="Old Password Is Incorrect"
            return render(request,'change_password.html',{'msg':msg},data)

    else:
        return render(request,'change_password.html',data)

def forgot_password(request):
    if request.method == 'POST':
        Email = request.POST['femail']
        try:
            user = User.objects.get(Email=Email)
            if user:
                global gen_otp
                email_Subject = "OTP For Reset Password From ApanuKhetar"
                gen_otp = randint(1000,9999) 
                print(gen_otp)
                sendmail(email_Subject,'otpVerification_emailTemplate',Email,{'name':user.FirstName,'gen_otp':gen_otp})
                return render(request,'get_otp.html',{'gen_otp':gen_otp,'femail':Email},data)
                
        except:
            msg = "This Email Address Not Register With US.Please Check your Email Address."
            return render(request,'get_email.html',{'msg':msg},data)
    else:
        return render(request,'get_email.html',data)

def chk_otp_forgot_password(request):
    votp = request.POST['fotp']
    vgen_otp = request.POST['gen_otp']
    vEmail = request.POST['femail']

    if votp == vgen_otp:
        return render(request, 'get_reset_password.html',{'femail':vEmail},data)
    else:
        msg = "OTP Is Invalid. Please Enter Valid OTP."
        return render(request,'get_otp.html',{'msg':msg},data)

def get_reset_password(request):
    if request.method == 'POST':
        v_new_pass=request.POST['fnewpass']
        v_confirm_pass = request.POST['fcnewpass']
        vEmail = request.POST['femail']
        
        user=User.objects.get(Email=vEmail) 
        if v_new_pass == v_confirm_pass:
            user.Password = v_new_pass
            user.save()
            msg="Password Reset Sucessfully."
            return render(request,'login.html',{'msg1':msg},data)
        else:
            msg="New Password And Confirm Password Is Not Matched."
            return render(request,'get_reset_password.html',{'femail':vEmail,'msg':msg},data)
        
