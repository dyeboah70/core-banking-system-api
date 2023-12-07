from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from transactions.models import Transactions
from transactions.decorators import is_teller
from django.core.paginator import Paginator
from django.core.cache import cache
from django.views.decorators.cache import cache_page


@csrf_exempt
@check_permission("view")
@is_teller
@cache_page(60 * 5)  # Cache the response for 5 minutes
def list_transactions(request, teller=None):

    cache_key = 'list_transactions'
    cached_response = cache.get(cache_key)

    if cached_response is not None:
        return JsonResponse(cached_response, safe=False)

    page_number = request.GET.get('page', 1)
    items_per_page = 10  # Define the number of transactions per page

    transactions = Transactions.objects.filter(
        teller_id=teller.profile_id).prefetch_related("user").values(
            "user__first_name", "user__last_name", "amount", "account_number",
            "date_created", "transaction_type",
            "reference_number").order_by('id')

    paginator = Paginator(transactions, items_per_page)
    page = paginator.get_page(page_number)

    transformed_transactions = [{
        "first_name":
        transaction["user__first_name"],
        "last_name":
        transaction["user__last_name"],
        "amount":
        transaction["amount"],
        "account_number":
        transaction["account_number"],
        "date_created":
        transaction["date_created"],
        "transaction_type":
        transaction["transaction_type"],
        "reference_number":
        transaction["reference_number"]
    } for transaction in page]

    response_data = {
        "message": "transactions listed successfully",
        "status": 200,
        "current_page": page.number,
        "total_pages": paginator.num_pages,
        "data": transformed_transactions,
    }

    cache.set(cache_key, response_data,
              60 * 5)  # Store the response in cache for 5 minutes

    return JsonResponse(response_data, safe=False)
