from django.shortcuts import render
from django.views import View 



class SalesView(View):
    def get(self,request):
        return render(request,"sales/saleslist.html")

class SalesListView(View):
    def get(self,request,slug):
        return render(request,"sales/saleslist.html")