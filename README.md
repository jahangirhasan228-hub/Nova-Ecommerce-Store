# 🌸 Nova E-Commerce Store

Nova is a simple pastel-themed e-commerce website built using Django.
It provides a smooth online shopping experience with product browsing, cart management, checkout, and order tracking.

## ✨ Features

* User Registration and Login
* User Logout
* Product Listing
* Product Details Page
* Product Image Upload
* Shopping Cart
* Checkout System
* Shipping Information Form
* Order Processing
* Order Confirmation
* My Orders Page
* Admin Product Management
* Responsive Pastel UI Design

## 🛠️ Technologies Used

* Python
* Django
* HTML
* CSS
* SQLite
* Bootstrap (UI Design)

## 📂 Project Structure

```
Nova
│
├── nova              # Django project folder
├── store             # Main application
├── templates         # HTML templates
├── static            # CSS files
├── media             # Uploaded product images
├── db.sqlite3        # Database
├── manage.py         # Django management file
├── requirements.txt  # Required Python packages
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

Download or clone this project from GitHub.

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create Admin Account

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

Open the website:

```
http://127.0.0.1:8000/
```

## 👩‍💻 Admin Panel

Admin panel can be accessed using:

```
http://127.0.0.1:8000/admin/
```

Admin can:

* Add products
* Update products
* Upload product images
* Manage orders

## 🌸 About Nova

Nova focuses on a calm and pleasant shopping experience with a pastel-themed interface and simple user-friendly design.

## 📌 Project Name

**Nova E-Commerce Store 🌸**

## © Copyright

© 2026 Nova Store. All Rights Reserved.
