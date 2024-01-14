from django.db import models
from django.contrib.auth.models import User #this is the deafult user model for django


# Create your models here.

#this is for the Customer table of the data model
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) #the OneToOneField here just means one to one relationship btw the user and the customer, meaning a user can only have one customer and a customer can only have one user
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    deliverable=models.BooleanField(default=False, null=True, blank=False)
    image=models.ImageField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
    
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderitems= self.orderitem_set.all()
        for i in orderitems:
            if i.product.deliverable == False:
                shipping = True
        return shipping
        
    
class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity=models.IntegerField(default=0, null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.product.name
    
    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total

   
class Shipping_address(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address=models.CharField(max_length=200, null=True, blank=True)
    city=models.CharField(max_length=200, null=True, blank=True)
    state=models.CharField(max_length=200, null=True, blank=True)
    zip_code=models.CharField(max_length=200,null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address


    



    


     
