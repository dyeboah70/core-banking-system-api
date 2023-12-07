from managers.models import Roles
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from managers.decorators import check_permission


@csrf_exempt
@check_permission("view")
def roles(request):
    roles = Roles.objects.all().values("id", "name")

    response_data = {
        "message": "Roles listed successfully",
        "status": 200,
        "data": list(roles),
    }

    return JsonResponse(response_data, status=200)
