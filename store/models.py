from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    name = models.CharField(max_length=100)

    price = models.IntegerField()

    description = models.TextField()

    image = models.ImageField(upload_to="products/")


    def __str__(self):
        return self.name



class Order(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)
    customer_name = models.CharField(max_length=100, blank=True, null=True)

    phone = models.CharField(max_length=15, blank=True, null=True)

    address = models.TextField(blank=True, null=True)

    city = models.CharField(max_length=50, blank=True, null=True)

    pincode = models.CharField(max_length=10, blank=True, null=True)


    ordered_date = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.customer_name + " - " + self.product.name