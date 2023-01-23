
from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include("accounts.urls",namespace="accounts")),
    
    path("dashboard/",include("dashboard.urls",namespace="dashboard")),
    path("dashboard/order/",include("orders.urls" ,namespace="orders")),  
    path("dashboard/vendors/",include("vendors.urls",namespace="vendors")),
    path("dashboard/products/",include("products.urls",namespace="products")),
    path("dashboard/sales/",include("sales.urls",namespace="sales")),
]
