from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from accounts.models import AccountTypes


@csrf_exempt
@check_permission("view")
def account_types(request):
    account_types = AccountTypes.objects.all().values("id", "account_type")

    response_data = {
        "message": "Account types listed sucessfully",
        "status": 200,
        "data": list(account_types),
    }

    return JsonResponse(response_data, status=200)
