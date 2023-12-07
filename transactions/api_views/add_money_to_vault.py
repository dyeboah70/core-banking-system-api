from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from managers.decorators import check_permission
from deposits.models import Vault


@csrf_exempt
@require_POST
@check_permission("add_money")
def add_to_vault(request):
    try:
        data = json.loads(request.body)
        amount = data.get("amount")

        if amount is None:
            return JsonResponse(
                {
                    "message": "Missing parameter in request",
                    "status": 400,
                },
                status=400,
            )

        Vault.objects.create(amount=amount)
        return JsonResponse(
            {
                "message": "Amount added to vault successfully",
                "status": 200,
            },
            status=200,
        )
    
    except json.JSONDecodeError:
        return JsonResponse({
            "message": "Missing parameter in request or no json object passed"
        })

    except Exception as e:
        return JsonResponse(
            {
                "message": str(e),
                "status": 400,
            },
            status=400,
        )
