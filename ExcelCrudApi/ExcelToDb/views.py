import pandas as pd
from django.db import transaction as db_transaction
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ExcelToDb.models import Transaction

@api_view(['POST'])
def bulk_insert(request):
    file = request.FILES.get('file')
    df = pd.read_excel(file,engine='openpyxl')
    df.rename(columns={
        'brand_id': 'brand_id',
        'user_name': 'user_name',
        'receive_time': 'receive_time',
        'upload_time': 'upload_time',
        'description': 'description',
        'amount': 'amount'
    }, inplace=True)
    print(df)
    transactions = [
        Transaction(
            brand_id=row['brand_id'],
            user_name=row['user_name'],
            receive_time=pd.to_datetime(row['receive_time'], errors='coerce'),
            upload_time = pd.to_datetime(row['upload_time'], errors='coerce'),
            description=row['description'],
            amount=row['amount'],
        )
        for index, row in df.iterrows()
    ]
    print(transactions)
    with db_transaction.atomic():
        Transaction.objects.bulk_create(transactions)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_transactions_export(request):
    transactions = Transaction.objects.all().values()
    result_df = pd.DataFrame(list(transactions))
    result_df['upload_time'] = result_df['upload_time'].dt.tz_localize(None)
    result_df['receive_time'] = result_df['receive_time'].dt.tz_localize(None)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="transactions.xlsx"'
    with pd.ExcelWriter(response,engine='openpyxl') as writer:
        result_df.to_excel(writer, index=False,sheet_name='Transactions')
    return response