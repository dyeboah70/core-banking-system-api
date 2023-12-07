from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.models import Managers
from managers.decorators import check_permission
from django.core.paginator import Paginator
from django.core.cache import cache


@csrf_exempt
@check_permission("view")
def list_staffs(request):
    page_number = request.GET.get('page', 1)
    items_per_page = 10  # Define the number of staff members per page

    # Check if the serialized data is already cached
    cache_key = f"staffs_list_{page_number}"
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data, safe=False)

    staffs = Managers.objects.all().prefetch_related("roles").values(
        "profile_id",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "staff_id",
        "roles__name"
    ).order_by('profile_id')  # Specify the desired ordering field

    paginator = Paginator(staffs, items_per_page)
    page = paginator.get_page(page_number)

    staff_list = []

    for staff_data in page:
        staff_data["roles"] = staff_data.pop("roles__name")
        staff_list.append(staff_data)

    response_data = {
        "message": "Staff listed successfully",
        "status": 200,
        "current_page": page.number,
        "total_pages": paginator.num_pages,
        "data": staff_list,
    }

    # Cache the serialized data for future requests
    cache.set(cache_key, response_data)

    return JsonResponse(response_data, safe=False)
