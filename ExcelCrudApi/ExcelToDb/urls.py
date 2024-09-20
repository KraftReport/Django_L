from django.urls import path

from ExcelToDb.views import bulk_insert, get_transactions_export

urlpatterns = [
    path('bulk-insert',bulk_insert,name='bulk_insert'),
    path('export',get_transactions_export, name='get_transactions_export')
]