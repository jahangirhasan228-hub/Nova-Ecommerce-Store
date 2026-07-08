from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Product, Order, SiteSettings


def _site_settings():
    try:
        return SiteSettings.load()
    except Exception:
        return None


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {
        "products": products,
        "site_settings": _site_settings(),
    })


def product(request, id):
    item = get_object_or_404(Product, id=id)
    return render(request, "product.html", {"product": item})


def add_cart(request, id):
    cart = request.session.get("cart", [])
    cart.append(id)
    request.session["cart"] = cart
    return redirect("cart")


def cart(request):
    ids = request.session.get("cart", [])
    products = Product.objects.filter(id__in=ids)
    total = sum(p.price for p in products)
    return render(request, "cart.html", {"products": products, "total": total})


def checkout(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        name    = request.POST["name"]
        phone   = request.POST["phone"]
        address = request.POST["address"]
        city    = request.POST["city"]
        pincode = request.POST["pincode"]

        ids = request.session.get("cart", [])
        products = Product.objects.filter(id__in=ids)

        for p in products:
            Order.objects.create(
                user=request.user, product=p, quantity=1,
                customer_name=name, phone=phone,
                address=address, city=city, pincode=pincode,
            )

        request.session["cart"] = []
        return render(request, "checkout_success.html")

    return render(request, "checkout.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        return redirect("login")
    return render(request, "register.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("home")


def my_orders(request):
    if not request.user.is_authenticated:
        return redirect("login")
    orders = Order.objects.filter(user=request.user).order_by("-ordered_date")
    return render(request, "orders.html", {"orders": orders})
