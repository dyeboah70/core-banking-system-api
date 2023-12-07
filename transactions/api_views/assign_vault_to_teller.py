from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from managers.decorators import check_permission
from deposits.models import Vault, TellerVault
from managers.models import Managers
from datetime import date
from django.db.models import F




@csrf_exempt
# @check_permission("add_money")
@require_POST
def assign_teller_vault(request):
    try:
        data = json.loads(request.body)
        staff_id = data.get("staff_id")
        amount = data.get("amount")

        teller = Managers.objects.get(staff_id=staff_id)
        is_teller = teller.roles.filter(name="TELLER").exists()

        if is_teller:
            today = date.today()
            if TellerVault.objects.filter(teller=teller, date_assigned=today).exists():
                response_data = {
                    "message": "Teller has already been assigned to the vault today",
                    "status": 400,
                }
            else:
                total_vault = Vault.objects.first()  # Assuming there is only one total vault instance
                
                if total_vault.amount < amount:
                    response_data = {
                        "message": "Assigned amount is greater than the available total vault amount",
                        "status": 400,
                    }
                else:
                    teller_vault = TellerVault.objects.create(teller=teller, amount=amount)
                    
                    # Deduct the assigned amount from the total vault
                    total_vault.amount = F('amount') - amount
                    total_vault.save()
                    
                    # # Assign the amount from the total vault to the teller's vault
                    # teller_vault.vault.amount = amount
                    # teller_vault.vault.save()

                    response_data = {
                        "message": "Teller assigned to the vault successfully",
                        "status": 200,
                        "data": {
                            "teller_vault_id": teller_vault.id,
                            "teller_name": teller_vault.get_full_name,
                            "vault_amount": teller_vault.amount,
                        },
                    }
        else:
            response_data = {
                "message": "The specified user is not a Teller",
                "status": 400,
            }

        return JsonResponse(response_data, safe=False)

    except json.decoder.JSONDecodeError:
        response_data = {
            "message": "Invalid data format",
            "status": 400,
        }

        return JsonResponse(response_data, safe=False)

    except Managers.DoesNotExist:
        response_data = {
            "message": "Invalid staff_id",
            "status": 404,
        }

        return JsonResponse(response_data, safe=False)