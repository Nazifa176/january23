from django.shortcuts import render
from django.views import View 


class VendorListView(View):
    def get(self,request):
        return render(request,"vendors/vendor_list.html")

class VendorDetailView(View):
    def get(self,request,slug):
        return render(request,"vendors/vendor_detail.html")
        