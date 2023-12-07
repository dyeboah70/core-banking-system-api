from django.contrib import admin
from deposits.models import Deposits, DepositType, Vault, TellerVault


admin.site.register(Deposits)
admin.site.register(DepositType)
admin.site.register(Vault)
admin.site.register(TellerVault)
