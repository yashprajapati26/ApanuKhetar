from django.shortcuts import render,redirect
from . models import *
from . utils import *
from random import *
from ApanuKhetarProject.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
# Create your views here.

data = {}
category = Category.objects.all()
sub_category = Sub_Category.objects.all()
products = Product.objects.all()
offers = offer.objects.all()
data['category'] = category
data['sub_category'] = sub_category
data['products'] = products
data['offer'] = offers
for i in products:
    for j in offers:
        if j.product.Product_Name == i.Product_Name:
            if j.offer_status == "Active":
                percentage = float(j.offer_Dicount_Percentage)
                product_price = float(i.Product_Price)
                offer_dic = float((product_price * percentage)/100)
                temp = float(product_price - offer_dic)
                j.offer_Dicount_Price = temp
                j.save()

def index(request):
    print(data['category'])
    return render(request, 'index.html',data)

def contact(request):
    if request.method == 'POST':
        vname = request.POST['fname']
        vemail = request.POST['email']
        vsubject = request.POST['fsubject']
        vmessage = request.POST['fmessage']
        Contact.objects.create(Name = vname,Email = vemail,Subject = vsubject,Message = vmessage)
        msg = "Send Message Sucessfully."
        return render(request, 'contact.html',{'msg':msg},data)

    else:
        return render(request, 'contact.html',data)

def blog(request):
    return render(request, 'blog.html',data)

def product_details(request):
    return render(request, 'product_details.html',data)


def product_details(request,pk):
    product = Product.objects.get(pk=pk)
    cat = product.Category
    more_products = Product.objects.filter(Category=cat)
    data['product'] = product
    data['more_products'] = more_products
    return render(request, 'product_details.html',data)


def shoping_cart(request):
    return render(request, 'shoping_cart.html',data)

def shop(request):
    pk=1
    cat = Category.objects.get(pk=pk)
    sub_cat = Sub_Category.objects.filter(Main_Category=cat)
    data['sub_cat']=sub_cat
    product = Product.objects.all()
    print(product)
    data['products_shop'] = product
    return render(request, 'shop.html',data)

def shop1(request,pk):
    cat = Category.objects.get(pk=pk)
    sub_cat = Sub_Category.objects.filter(Main_Category=cat)
    data['sub_cat']=sub_cat
    print(sub_cat)
    sc = ""
    for i in sub_cat:
        sc = i
        break
    try:
        product = Product.objects.filter(Category=sc)
        print(product)
        data['products_shop'] = product
        msg = ""
        data['msg'] = msg
        return render(request, 'shop.html',data)
    except:
        msg = "Products Not Available."
        data['msg'] = msg
        return render(request, 'shop.html',data)

def shop2(request,pk):
    sub = Sub_Category.objects.get(pk=pk)
    print(sub)
    cat=sub.Main_Category.Category_Name
    cat1 = Category.objects.get(Category_Name=cat)
    sub_cat = Sub_Category.objects.filter(Main_Category=cat1)
    data['sub_cat']=sub_cat
    
    product = Product.objects.filter(Category=sub)
    print(product)
    
    data['products_shop'] = product
    return render(request, 'shop.html',data)

def logout(request):
    del request.session['email']
    del request.session['name']
    del request.session['total_wishlist']
    del request.session['total_cart']

    return render(request,'index.html',data)

def login(request):
    

    if request.method == 'POST':
        Email = request.POST['femail']
        Password = request.POST['fpassword']
        
        try:
            user = User.objects.get(Email=Email,Password=Password)
            wishlist=WishList.objects.filter(user=user)
            cart = Cart.objects.filter(user=user)
            if user.Status == 'Active':
                request.session['name']=user.FirstName
                request.session['email']=user.Email
                request.session['total_wishlist']=len(wishlist)
                request.session['total_cart']=len(cart)

                # print(request.POST['next'])
                # if 'next' in request.POST:
                #     return redirect(request.POST['next'])

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
                msg="Password Wrong.Please Enter Valid Password."
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
    
    if request.method == 'POST':
        vfname = request.POST['fname']
        vlname = request.POST['lname']
        vdob = request.POST['fDOB']
        vcountry = request.POST['fcountry']
        vmobile = request.POST['fmobile']

        if vfname != "" and vlname != "":
            user.FirstName = vfname
            user.LastName = vlname
            user.DOB = vdob
            user.Country = vcountry
            user.Mobile = vmobile
            user.save()
            msg = "Saved Changes"
            return render(request,'myaccount.html',{'user':user,'msg':msg})

        else:
            return render(request,'myaccount.html',{'user':user})

    else:
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

def mywishlist(request):
    try:
        user = User.objects.get(Email = request.session['email'])
        wishlist=WishList.objects.filter(user=user)
        request.session['total_wishlist']=len(wishlist)
        return render(request,'mywishlist.html',{'wishlist':wishlist})
    except:
        msg = "User Must Be Login for use Wishlist Features."
        return render(request, 'login.html',{'msg1':msg},data)

def add_to_wishlist(request,pk):
    product = Product.objects.get(pk=pk)
    try:
        user = User.objects.get(Email = request.session['email'])
        wishlist = WishList.objects.filter(user= user)
        for i in wishlist:
            if i.product.pk==product.pk:
                msg="Product Is Already In Your WishList"
                request.session['total_wishlist']=len(wishlist)
                return render(request,'mywishlist.html',{'wishlist':wishlist,'msg':msg})
        WishList.objects.create(user=user,product=product) 
        wishlist=WishList.objects.filter(user=user)
        request.session['total_wishlist']=len(wishlist)
        msg = "Added To Wishlist."
        return render(request,'mywishlist.html',{'wishlist':wishlist,'msg':msg})
    except Exception as e:
        print("-->",e)
        print("User Must Be Login...")
        msg = "User Must Be Login for use Wishlist Features."
        return render(request, 'login.html',{'msg1':msg},data)



def remove_from_wishlist(request,pk):
	wishlist = WishList.objects.get(pk=pk)
	wishlist.delete()
	return redirect('mywishlist')


def mycart(request):
    try:
        user = User.objects.get(Email = request.session['email'])
        cart=Cart.objects.filter(user=user).order_by("-id")
        print(cart)
        net_total = 0 

        for i in cart:
            i.after_dicount_price = i.product.Product_Price
            print("A")
            
            for j in offers:
                if j.product.Product_Name == i.product.Product_Name:
                    if j.offer_status == "Active":
                        i.discount_percentage = j.offer_Dicount_Percentage
                        i.after_dicount_price = j.offer_Dicount_Price
                        i.save()
            
            # count netprice 
            temp = float(i.total_price)
            print(temp)
            net_total = net_total + temp
            print(net_total)
            i.save()
                    
        request.session['total_cart']=len(cart)
        print(">>Showing Carts Item")
        return render(request,'shoping_cart.html',{'cart':cart,'net_total':net_total,'offer':offers})
    except Exception as e:
        print(">>",e)
        msg = "User Must Be Login for use Cart Features."
        return render(request, 'login.html',{'msg1':msg},data)

def update_qty_in_cart(request,pk):
    cart = Cart.objects.get(pk=pk)
    user = User.objects.get(Email=request.session['email'])
    qty = int(request.POST['fqty'])
    if qty <= cart.product.Product_Quantity:
        cart.qty = qty
        cart.total_price= qty * float(cart.after_dicount_price)
        print(cart.total_price)
        cart.save()
        print("Go To MyCart")
        return redirect('mycart')
    else:
        msg="Only "+str(cart.product.Product_Quantity)+" Quantity Left In Stock"
        return render(request,'shoping_cart.html',{'cart':cart,'msg':msg,'offer':offers})



def add_to_cart(request,pk):
    product = Product.objects.get(pk=pk)
    
    try:
        user = User.objects.get(Email = request.session['email'])
        if user:
            cart = Cart.objects.filter(user=user,status="pending")
            for i in cart:
                if i.product.pk==product.pk:
                    msg="Product is Already In Your Cart."
                    request.session['total_cart']=len(cart)
                    print(">>Already")
                    return render(request,'shoping_cart.html',{'cart':cart,'msg':msg,'offer':offers})

            if request.method == 'POST':
                vqty = int(request.POST['fqty'])
                price=float(product.Product_Price)
                total_price = float(price * vqty)

                for i in offers:
                    if i.product.Product_Name == product.Product_Name:
                        if i.offer_status == "Active":
                            temp = float(i.offer_Dicount_Price)
                            total_price = float(temp * vqty)



                Cart.objects.create(user=user,product=product,qty=vqty,price=price,total_price=total_price)
                print(">>Added To Cart (qty+)")
                return redirect('mycart')
            else:
                price=product.Product_Price
                total_price=product.Product_Price

                for i in offers:
                    if i.product.Product_Name == product.Product_Name:
                        if i.offer_status == "Active":
                            price = i.offer_Dicount_Price
                            total_price = i.offer_Dicount_Price

                Cart.objects.create(user=user,product=product,price=price,total_price=total_price)
                print(">>Added To Cart")
                return redirect('mycart')


    except Exception as e:
        print("-->",e)
        print("User Must Be Login...")
        msg = "User Must Be Login for use Cart Features."
        return render(request, 'login.html',{'msg1':msg},data)


def remove_from_cart(request,pk):
	cart=Cart.objects.get(pk=pk)
	cart.delete()
	return redirect('mycart')

def checkout(request):
    user = User.objects.get(Email=request.session['email'])
    cart = Cart.objects.filter(user=user,status="pending")
    net_total1 = 0
    tax_percentage = 5
    tax = 0
    for i in cart:
        temp = float(i.total_price)
        net_total1 = float(net_total1 + temp)    

    tax = float(net_total1 * tax_percentage)
    net_total2 = net_total1 + tax          
    return render(request, 'checkout.html',{'cart':cart,'user':user,'net_total':net_total2,'sub_total':net_total1,'tax':tax})


client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))


def pay(request):
    user = User.objects.get(Email=request.session['email'])
    cart = Cart.objects.filter(user=user,status="pending")
    print(cart)
    if request.method == "POST":
        vfname = request.POST['ffname']
        vlname = request.POST['flname']
        vcountry = request.POST['fcountry']
        vaddress = request.POST['faddress']
        vmno = request.POST['fmno']
        vpayment_method = request.POST['payment_method']
        
        if vfname != "" and vlname!= "" and vcountry != "" and vaddress != "" and vmno != "":
            user.FirstName = vfname
            user.LastName = vlname
            user.Address = vaddress
            user.Mobile = vmno
            user.Country = vcountry
            user.save()

            
            net_total1 = 0
            tax_percentage = 5
            tax = 0
            for i in cart:
                temp = float(i.total_price)
                net_total1 = float(net_total1 + temp) 

            tax = float(net_total1 * tax_percentage)
            net_total2 = net_total1 + tax    

            if vpayment_method == "Online": 
                 
                order_amount = int(net_total2)
                order_currency = "INR"
                payment_order = client.order.create(dict(amount=order_amount*100,currency=order_currency,payment_capture=1))
                payment_order_id = payment_order['id']
                return render(request,'pay.html',{'amount':order_amount,'payment_order':payment_order,'user':user})

            else:
                Email = user.Email
                email_Subject = "Order Sucessfully Done[cash on dilivery]"
                sendmail(email_Subject,'otpVerification_emailTemplate',Email,{'name':user.FirstName})
                return render(request,'invoice.html',{'user':user,'cart':cart,'net_total':net_total1})

        return render(request, 'checkout.html',{'cart':cart,'user':user})

def invoice(request):
    user = User.objects.get(Email=request.session['email'])
    cart = Cart.objects.filter(user=user,status="pending")
    print(cart)
    Razorpay_order_id = request.POST['razorpay_order_id']
    Razorpay_payment_id = request.POST['razorpay_payment_id']
    Razorpay_signature =  request.POST['razorpay_signature']
    net_price  = request.POST['amount'] 

    client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
    verification = {
		'razorpay_order_id': request.POST['razorpay_order_id'],
		'razorpay_payment_id': request.POST['razorpay_payment_id'],
		'razorpay_signature': request.POST['razorpay_signature']
	}

    try:
        Email = user.Email
        email_Subject = "Order Sucessfully Done.[online payment]"
        status = client.utility.verify_payment_signature(verification)
        sendmail(email_Subject,'otpVerification_emailTemplate',Email,{'name':user.FirstName})
        for i in cart:
            print(i)
            i.status = "Done"
            i.save()
            return render(request,'invoice.html',{'net_total':net_price,'cart':cart,'user':user})
    except Exception as e:
        print(e)
        msg ="Please Try Again.Somothing was Wrong! "
        return render (request,'checkout.html',{'msg':msg,'user':user,'cart':cart,'net_total':net_price})
        

