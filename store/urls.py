from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('product/<int:id>/', views.product, name='product'),

    path('add/<int:id>/', views.add_cart, name='add'),

    path('cart/', views.cart, name='cart'),

    path('checkout/', views.checkout, name='checkout'),
    path("register/", views.register, name="register"),

    path("login/", views.user_login, name="login"),

    path("logout/", views.user_logout, name="logout"),
    path("orders/", views.my_orders, name="orders"),

]