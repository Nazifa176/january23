from django.shortcuts import render
from django.views import View 


class ProductsView(View):
    def get(self,request):
        return render(request,"products/products.html")

class ProductsReviews(View):
    def get(self,request):
        return render(request,"products/products_reviews.html")

class ProductsAdd(View):
    def get(self, request):
        return render(request,"products/products_add.html")