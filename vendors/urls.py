from django.urls import path 

from .views import *

app_name="vendors"
urlpatterns=[
   path("",VendorListView.as_view(),name="vendor_list"),
   path("<slug:slug>/",VendorDetailView.as_view(),name="vendor_detail")
]