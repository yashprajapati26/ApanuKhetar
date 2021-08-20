from django.shortcuts import render
from . models import *
from . utils import *
from random import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def shop_details(request):
    return render(request, 'shop_details.html')

def logout(request):
    del request.session['email']
    del request.session['name']
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        Email = request.POST['femail']
        Password = request.POST['fpassword']
        
        try:
            user = User.objects.get(Email=Email,Password=Password)
            if user.Status == 'Active':
                request.session['name']=user.FirstName
                request.session['email']=user.Email
               
                print(request.session['email'])
                return render(request,'index.html')
            else:
                msg="your account is not active"
                global gen_otp
                email_Subject = "OTP For Login Verification From ApanuKhetar"
                gen_otp = randint(1000,9999) 
                print(gen_otp)
                sendmail(email_Subject,'otpVerification_emailTemplate',Email,{'name':user.FirstName,'gen_otp':gen_otp})
                return render(request, 'otp_signup.html',{'gen_otp':gen_otp,'femail':Email})
                
        except Exception as e:
            print(e)
            if Email=="" and Password=="":
                msg="please enter all fileds"
                return render(request,'login.html',{'msg1':msg})
            else:
                msg="somothing wrong."
                return render(request,'login.html',{'msg1':msg})
            
        # return render(request, 'index.html')
    else:
        return render(request, 'login.html')

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
                return render(request,'login.html',{'msg':msg})
        except:
            if u.FirstName=="" or u.LastName=="" or u.Email=="" or u.Password=="" or ConfirmPassword=="":
                msg="please enter all details!"
                return render(request,'login.html',{'msg':msg})
            elif u.Password == ConfirmPassword:
                # User.objects.create(FirstName=u.FirstName, LastName=u.LastName, Email=u.Email, Password=u.Password)
                global gen_otp
                email_Subject = "OTP For SignUp Verification From ApanuKhetar"
                gen_otp = randint(1000,9999) 
                print(gen_otp)
                sendmail(email_Subject,'otpVerification_emailTemplate',u.Email,{'name':u.FirstName,'gen_otp':gen_otp})
                return render(request, 'otp_signup.html',{'gen_otp':gen_otp})
            else:
                msg="password & confirm password does not match"
                return render(request,'login.html',{'msg':msg})
    
    else:
        return render(request, 'login.html')



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
            return render(request,'index.html')

        if votp == vgen_otp:
            user=User.objects.create(FirstName=u.FirstName, LastName=u.LastName, Email=u.Email, Password=u.Password, Status="Active")
            request.session['name']=user.FirstName
            request.session['email']=user.Email

            print(request.session.name)
            print(request.session.email)

            print(user)
            return render(request,'index.html')
        else:
            msg="OTP is Wrong. Please Enter Valid OTP."
            return render(request,'otp_signup.html',{'msg':msg,'gen_otp':vgen_otp})
    else:
        return render(request,'otp_signup.html')

def myaccount(request):
    return render(request,'myaccount.html')
