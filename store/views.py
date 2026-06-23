from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def home(request):
    products = Product.objects.all()
    return render(request,"home.html",{"products":products})


def product(request,id):
    item = Product.objects.get(id=id)
    return render(request,"product.html",{"product":item})


def add_cart(request,id):
    cart=request.session.get("cart",[])
    cart.append(id)
    request.session["cart"]=cart
    return redirect("cart")


def cart(request):

    ids = request.session.get("cart", [])

    products = Product.objects.filter(id__in=ids)

    total = sum(product.price for product in products)

    return render(request, "cart.html", {
        "products": products,
        "total": total
    })


def checkout(request):

    if not request.user.is_authenticated:
        return redirect("login")


    if request.method == "POST":

        name = request.POST["name"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        city = request.POST["city"]
        pincode = request.POST["pincode"]


        ids = request.session.get("cart", [])

        products = Product.objects.filter(id__in=ids)


        for product in products:

            Order.objects.create(

                user=request.user,

                product=product,

                quantity=1,

                customer_name=name,

                phone=phone,

                address=address,

                city=city,

                pincode=pincode

            )


        request.session["cart"] = []


        return render(
            request,
            "checkout_success.html"
        )


    return render(request,"checkout.html")

def register(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )

        user.save()

        return redirect("login")


    return render(request,"register.html")



def user_login(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(
            username=username,
            password=password
        )


        if user:

            login(request,user)

            return redirect("home")


    return render(request,"login.html")



def user_logout(request):

    logout(request)

    return redirect("home")

def my_orders(request):

    if not request.user.is_authenticated:
        return redirect("login")


    orders = Order.objects.filter(
        user=request.user
    ).order_by("-ordered_date")


    return render(request, "orders.html", {
        "orders": orders
    })