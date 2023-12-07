from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission
from deposits.models import Vault, TellerVault

# @csrf_exempt
# @check_permission("view")
# def vaults(request):
#     vaults = Vault.objects.all().values("id", "amount")

#     response_data = {
#         "message": "Vault amount listed successfully",
#         "status": 200,
#         "data": list(vaults),
#     }

#     return JsonResponse(response_data, status=200)


@csrf_exempt
@check_permission("view")
def vaults(request):
    vaults = TellerVault.objects.all().values("id", "teller__staff_id", "vault__amount")

    transform_vaults = [{
        "id": vault["id"],
        "staff_id": vault["teller__staff_id"],
        "amount": vault["vault__amount"]
    } for vault in vaults]

    response_data = {
        "message": "Teller vaults listed successfully",
        "status": 200,
        "data": transform_vaults,
    }

    return JsonResponse(response_data, status=200)