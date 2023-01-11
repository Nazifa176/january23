from django.shortcuts import render
from django.views import View



# Create your views here.

class OrderListView(View):
    def get(self,request):
        return render(request,"orders/order_list.html")



class OrderDetailsView(View):
    def get(self,request,id):
        return render(request,"orders/order_details.html")
