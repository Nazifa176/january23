from django.shortcuts import render
from django.views import View 


class FinancialYearView(View):
    def get(self,request):
        return render(request,"accounts/financial_year.html")

class SubAccountView(View):
    def get(self,request):
        return render(request,"accounts/sub_account.html")

class PredifiendAccountView(View):
    def get(self,request):
        return render(request,"accounts/predefined_account.html")

class DebitVoucherView(View):
    def get(self,request):
        return render(request,"accounts/debit_voucher.html")

class CrebitVoucherView(View):
    def get(self,request):
        return render(request,"accounts/credit_voucher.html")

class ContraView(View):
    def get(self,request):
        return render(request,"accounts/contra_voucher.html")
        
class JournalVoucherView(View):
    def get(self,request):
        return render(request,"accounts/journal_voucher.html")

class BankReconcilationView(View):
    def get(self,request):
        return render(request,"accounts/bank_reconcilation.html")

class OpeningBalanceView(View):
    def get(self,request):
        return render(request,"accounts/opening_balance.html")

