from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from accounts.models import Accounts
from django.core.paginator import Paginator
from django.core.cache import cache
from django.views.decorators.http import require_POST


@csrf_exempt
@check_permission("view")
@require_POST
def list_accounts(request):
    page_number = request.GET.get('page', 1)
    items_per_page = 10  # Define the number of accounts per page

    # Check if the serialized data is already cached
    cache_key = f"accounts_list_{page_number}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data, safe=False)

    accounts = Accounts.objects.select_related('user').values(
        "user__first_name",
        "user__last_name",
        "balance",
        "account_number",
        "date_created",
    ).order_by("account_number")  # Specify the desired ordering field

    paginator = Paginator(accounts, items_per_page)
    page = paginator.get_page(page_number)

    account_list = []

    for account_data in page:
        account_data["first_name"] = account_data.pop("user__first_name")
        account_data["last_name"] = account_data.pop("user__last_name")
        account_list.append(account_data)

    response_data = {
        "message": "Accounts listed successfully",
        "status": 200,
        "current_page": page.number,
        "total_pages": paginator.num_pages,
        "data": account_list,
    }

    # Cache the serialized data for future requests
    cache.set(cache_key, response_data)

    return JsonResponse(response_data, safe=False)
