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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.product.name}"


class SiteSettings(models.Model):
    """Singleton: global site config managed from Django admin panel."""
    facebook_url    = models.URLField(blank=True, null=True, verbose_name="Facebook Page URL")
    instagram_url   = models.URLField(blank=True, null=True, verbose_name="Instagram Profile URL")
    whatsapp_number = models.CharField(
        max_length=20, blank=True, null=True,
        verbose_name="WhatsApp Number",
        help_text="Include country code, e.g. 8801XXXXXXXXX"
    )
    youtube_url = models.URLField(blank=True, null=True, verbose_name="YouTube Channel URL")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Kroy Shindhu — Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1  # singleton
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class PaymentMethod(models.Model):
    PAYMENT_CHOICES = [
        ('bkash',  'bKash'),
        ('nagad',  'Nagad'),
        ('rocket', 'Rocket'),
        ('upay',   'Upay'),
    ]

    name = models.CharField(
        max_length=20, choices=PAYMENT_CHOICES, unique=True,
        verbose_name="Payment Gateway"
    )
    is_enabled = models.BooleanField(
        default=True, verbose_name="Enable this payment method"
    )
    merchant_number = models.CharField(
        max_length=20, blank=True,
        verbose_name="Merchant Mobile Number",
        help_text="The registered merchant/agent number"
    )
    merchant_id = models.CharField(
        max_length=100, blank=True,
        verbose_name="Merchant ID / API Key",
        help_text="Optional — for API integration"
    )

    class Meta:
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"

    def __str__(self):
        return self.get_name_display()
