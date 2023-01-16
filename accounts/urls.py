from django.urls import path 

from .views import *

app_name="accounts"

urlpatterns=[
    path("financial-year/",FinancialYearView.as_view(),name="financial-year"),
    path("sub-accounts/",SubAccountView.as_view(),name="sub-account"),
    path("predifiend-accounts/",PredifiendAccountView.as_view(),name="predifind-account"),
    path("credit-voucher/",CrebitVoucherView.as_view(),name="credit-voucher"),
    path("debit-voucher/",DebitVoucherView.as_view(),name="debit-voucher"),
    path("contra-voucher/",ContraView.as_view(),name="contra-voucher"),
    path("opening-balance/",OpeningBalanceView.as_view(),name="opening-balance"),
    path("journal-voucher/",JournalVoucherView.as_view(),name="journal-voucher"),
    path("chart-of-accounts/",ChartOfAccountView.as_view(),name="chart-of-account"),
    path("bank-reconcilation/",BankReconcilationView.as_view(),name="bank-reconcilation"),
]