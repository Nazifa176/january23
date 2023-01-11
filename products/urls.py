from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
        path("",ProductsView.as_view(),name="products"),
        path("reviews/",ProductsReviews.as_view(),name="products_reviews"),
        path("add-products/",ProductsAdd.as_view(),name="add_products"),
]