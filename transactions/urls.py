from django.urls import path
from transactions.api_views.deposit import create_transaction
from transactions.api_views.transactions import list_transactions
from withdrawals.api_views.withdrawal import create_withdrawal
from transactions.api_views.deposit_between_accounts import create_transaction_between_accounts
from transactions.api_views.transactions_by_search import transactions_by_search
from transactions.api_views.transaction_statement import transaction_statement
from transactions.api_views.deposit_types import deposit_types
from transactions.api_views.add_money_to_vault import add_to_vault
from transactions.api_views.vaults import vaults
from transactions.api_views.assign_vault_to_teller import assign_teller_vault
from transactions.api_views.teller_only_vault import teller_vault
from transactions.api_views.deposit_with_vault import deposit
from transactions.api_views.withdrawal_with_vault import withdrawal_with_vault

app_name = 'transactions'
urlpatterns = [
    path('deposit/', create_transaction, name='deposit'),
    path("deposit-with-vault/", deposit, name="deposit-with-vault"),
    path('withdrawal-with-vault/', withdrawal_with_vault, name='withdrawal-with-vault'),
    path('vaults/', vaults, name='vaults'),
    path('teller-vault/', teller_vault, name='teller-vault'),
    path('assign-vault-to-teller/', assign_teller_vault, name='assign-vault-to-teller'),
    path('add-money-to-vault/', add_to_vault, name='add-money-to-vault'),
    path('deposit-types/', deposit_types, name='deposit-types'),
    path('transactions-by-search/',
         transactions_by_search,
         name='transactions-by-search'),
    path('transactions/', list_transactions, name='transactions'),
    path('transaction-statement/',
         transaction_statement,
         name='transaction-statement'),
    path('withdrawal/', create_withdrawal, name='withdrawal'),
    path('deposit-between-accounts/',
         create_transaction_between_accounts,
         name='deposit-between-accounts'),
]
