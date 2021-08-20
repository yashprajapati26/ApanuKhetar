from django.db import models

# Create your models here.

class User(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=20)
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
    sub_cat_image = models.ImageField(upload_to='Product_Images/',default="default.png")

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
    Product_image_2=models.ImageField(upload_to='Product_Images/',null=True,blank=True)
    Product_image_3=models.ImageField(upload_to='Product_Images/',null=True,blank=True)
    Product_image_4=models.ImageField(upload_to='Product_Images/',null=True,blank=True)
    Discount_Percentage = models.FloatField(null=True,blank=True)
    Discount_Amount = models.FloatField(null=True,blank=True)
    After_Discount = models.FloatField(null=True,blank=True)
    Tax_Percentage = models.FloatField(null=True,blank=True)
    Tax_Amount = models.FloatField(null=True,blank=True)
    Final_Amount = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.Product_Name + " | " + self.Category.Main_Category.Category_Name + " > " + self.Category.Sub_Category_Name



