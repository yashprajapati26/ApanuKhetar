from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=20)
    Country = models.CharField(max_length=30,blank=True, null=True)
    Mobile = models.IntegerField(blank=True,null=True)
    Address = models.CharField(max_length=300,null=True,blank=True)
    Shipping_Address = models.CharField(max_length=300,null=True,blank=True)
    Status = models.CharField(max_length=10,default="Deactive")

    def __str__(self):
        return self.Email + " | " + self.FirstName

class Category(models.Model):
    Category_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Category_Name

class Sub_Category(models.Model):
    Main_Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Sub_Category_Name = models.CharField(max_length=100)
    sub_cat_image = models.ImageField(upload_to='Product_Images/',default="default.jpg")

    def __str__(self):
        return self.Sub_Category_Name + " | " + self.Main_Category.Category_Name

class Product(models.Model):
    CHOICES1 = (
        ("In Stock",'In Stock'),
        ("Out of Stock",'Out of Stock'),
    )
    Category = models.ForeignKey(Sub_Category,on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=100)
    Product_Brand_Name = models.CharField(max_length=100,blank=True) 
    Product_Desc = models.TextField(max_length=500)
    Product_Price  = models.IntegerField()
    Product_Stock = models.CharField(max_length=20,choices=CHOICES1,default="In Stock")
    Product_Quantity = models.IntegerField(default=100)
    Product_image_1=models.ImageField(upload_to='Product_Images/',null=True)
    Product_image_2=models.ImageField(upload_to='Product_Images/',null=True,blank=True,default="default.jpg")
    Product_image_3=models.ImageField(upload_to='Product_Images/',null=True,blank=True)
    Product_image_4=models.ImageField(upload_to='Product_Images/',null=True,blank=True)

    def __str__(self):
        return self.Product_Name + " | " + self.Category.Main_Category.Category_Name + " > " + self.Category.Sub_Category_Name


class WishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    added_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.FirstName+" - "+self.product.Product_Name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    added_date=models.DateTimeField(default=timezone.now)
    qty=models.CharField(max_length=100,default="1")
    price=models.CharField(max_length=100,default="")
    discount_percentage = models.CharField(max_length=10,default="0")
    after_dicount_price = models.CharField(max_length=10,default="0")

    total_price=models.CharField(max_length=100,default="0")
    status=models.CharField(max_length=10,default="pending")

    def __str__(self):
        return self.user.FirstName+" - "+self.product.Product_Name
    
class Contact(models.Model):
    Name=models.CharField(max_length=15)
    Email=models.CharField(max_length=30)
    Subject=models.CharField(max_length=150)
    Message=models.TextField(max_length=500)

    def __str__(self):
        return self.Email

class offer(models.Model):
    CHOICES1 = (
        ("Active",'Active'),
        ("Deactive",'Deactive'),
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    offer_name = models.CharField(max_length=30)
    offer_status = models.CharField(max_length=10,choices=CHOICES1,default="Active")
    offer_dicription = models.CharField(max_length=300)
    offer_Dicount_Percentage = models.CharField(max_length=10)
    offer_Dicount_Price = models.CharField(max_length=10) #Here Save Price After discount
    start_date = models.DateTimeField(auto_now_add=True)
    ended_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.offer_name

class news(models.Model):

    Title = models.CharField(max_length=50)
    Discription = models.CharField(max_length=500)
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Title