from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from transactions.models import Transactions
from transactions.decorators import is_teller
from django.db.models import Q


@csrf_exempt
@check_permission("view")
@is_teller
def transactions_by_search(request, teller=None):
    search_date = request.GET.get(
        "date")  # Get the search date from query parameters
    search_type = request.GET.get(
        "type")  # Get the search transaction type from query parameters

    transactions = Transactions.objects.filter(teller_id=teller.profile_id)

    if search_date or search_type:
        query = Q()
        if search_date:
            query |= Q(date_created=search_date)
        if search_type:
            query |= Q(transaction_type=search_type)

        transactions = transactions.filter(query)

    transactions = transactions.values("user__first_name", "user__last_name",
                                       "amount", "account_number",
                                       "date_created", "transaction_type",
                                       "reference_number")

    response_data = {
        "message": "Transactions listed successfully",
        "status": 200,
        "data": list(transactions),
    }

    return JsonResponse(response_data, safe=False)
