from django.shortcuts import render
from django.views import View 


class DashBoardView(View):
    def get(self,request):
        return render(request,"dashboard/dashboard.html")
    