from django.db.models import Sum

from transactions.models import *


def get_total_balance(user):
    total = user.operations.aggregate(Sum('amount'))['amount__sum']
    if not total:
        total = 0
    return total
