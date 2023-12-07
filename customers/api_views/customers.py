from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from accounts.models import Accounts
from django.core.paginator import Paginator
from django.core.cache import cache


@csrf_exempt
@check_permission("view")
def list_customers(request):
    page_number = request.GET.get('page', 1)
    items_per_page = 10  # Define the number of customers per page

    # Check if the serialized data is already cached
    cache_key = f"customers_list_{page_number}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data, safe=False)

    customers = Accounts.objects.all().select_related("user").values(
        "user__profile_id",
        "user__email",
        "user__first_name",
        "user__last_name",
        "user__mobile_number",
        "user__city",
        "account_number",
        "balance",
        "user__is_approved"
    ).order_by('user_id')

    paginator = Paginator(customers, items_per_page)
    page = paginator.get_page(page_number)

    transformed_customers = [
        {
            "profile_id": customer["user__profile_id"],
            "email": customer["user__email"],
            "first_name": customer["user__first_name"],
            "last_name": customer["user__last_name"],
            "mobile_number": customer["user__mobile_number"],
            "city": customer["user__city"],
            "account_number": customer["account_number"],
            "balance": customer["balance"],
            "is_approved": customer["user__is_approved"],
        }
        for customer in page
    ]

    response_data = {
        "message": "customers listed successfully",
        "status": 200,
        "current_page": page.number,
        "total_pages": paginator.num_pages,
        "data": transformed_customers,
    }

    # Cache the serialized data for future requests
    cache.set(cache_key, response_data)

    return JsonResponse(response_data, safe=False)
