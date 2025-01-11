# from django.db import models

# # Create your models here.


# class Products(models.model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     stock = models.IntegerField()
#     category = models.ForeignKey('Category', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name


# class Order(models.Model):
#     product = models.ForeignKey('Products', on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     total = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.product.name


# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15)
#     address = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class OrderItem(models.Model):
#     product = models.ForeignKey('Products', on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     total = models.DecimalField(max_digits=10, decimal_places=2)
#     order = models.ForeignKey('Order', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.product.name


# class ShippingAddress(models.Model):
#     customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
#     order = models.ForeignKey('Order', on_delete=models.CASCADE)
#     address = models.TextField()
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.customer.name
