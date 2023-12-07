from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from transactions.decorators import is_teller
from deposits.models import TellerVault


@csrf_exempt
@check_permission("view")
@is_teller
def teller_vault(request, teller=None):
    vault = TellerVault.objects.filter(teller=teller)
    vault_amount = vault.values("amount")
    response_data = {
        "message": "Teller vaults",
        "status": 200,
        "data": list(vault_amount),
    }

    return JsonResponse(response_data, safe=False)
