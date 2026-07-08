from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Order, SiteSettings, PaymentMethod

# ── Admin branding ─────────────────────────────────────────────────────────────
admin.site.site_header  = "Kroy Shindhu Admin"
admin.site.site_title   = "Kroy Shindhu"
admin.site.index_title  = "Dashboard"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ('name', 'price', 'image_preview')
    search_fields = ('name',)
    list_per_page = 25

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:48px;border-radius:6px;" />', obj.image.url
            )
        return "—"
    image_preview.short_description = "Preview"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display   = ('customer_name', 'product', 'quantity', 'phone', 'city', 'ordered_date')
    list_filter    = ('ordered_date', 'city')
    search_fields  = ('customer_name', 'phone', 'product__name')
    readonly_fields = ('ordered_date',)
    list_per_page  = 30


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Social Media Links", {
            "fields": ("facebook_url", "instagram_url", "whatsapp_number", "youtube_url"),
            "description": (
                "Enter full URLs (e.g. https://facebook.com/yourpage). "
                "Leave blank to hide the link from the footer."
            ),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = SiteSettings.load()
        from django.shortcuts import redirect
        return redirect(f"/admin/store/sitesettings/{obj.pk}/change/")


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display  = ('gateway_name', 'is_enabled', 'merchant_number', 'merchant_id')
    list_editable = ('is_enabled', 'merchant_number', 'merchant_id')
    list_per_page = 10

    fieldsets = (
        (None, {"fields": ("name", "is_enabled")}),
        ("Credentials", {
            "fields": ("merchant_number", "merchant_id"),
            "description": (
                "Enter the merchant credentials provided by the payment gateway. "
                "Stored securely in the database."
            ),
        }),
    )

    def gateway_name(self, obj):
        return format_html("<strong>{}</strong>", obj.get_name_display())
    gateway_name.short_description = "Gateway"
    gateway_name.admin_order_field = "name"
