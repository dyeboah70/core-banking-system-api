from django.contrib import admin
from loans.models import Loan, Repayment, LoanType

admin.site.register(Loan)
admin.site.register(Repayment)
admin.site.register(LoanType)
