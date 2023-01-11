from django.urls import path
from .views import *

app_name="orders"

urlpatterns=[
    path("",OrderListView.as_view(),name="orders"),
    path("details/<int:id>",OrderDetailsView.as_view(),name="order_detail"),
]