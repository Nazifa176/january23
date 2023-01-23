from django.urls import path 

from .views import *

app_name="sales"

urlpatterns=[
    path("", SalesView.as_view(),name="dashboard"),
    path("saleslist", SalesListView.as_view(),name="dashboard"),

]






    


   
    
