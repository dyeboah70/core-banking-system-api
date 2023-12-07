from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from deposits.models import DepositType


@csrf_exempt
@check_permission("view")
def deposit_types(request):
    account_types = DepositType.objects.all().values("id", "name")

    response_data = {
        "message": "Deposit types listed sucessfully",
        "status": 200,
        "data": list(account_types),
    }

    return JsonResponse(response_data, status=200)
