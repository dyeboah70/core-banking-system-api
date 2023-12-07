from transactions.models import Transactions
from transactions.constants import INTEREST
from accounts.models import Accounts
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from celery import shared_task
from my_package.config.json_reader import read_config
from twilio.rest import Client
import os


@shared_task(routing_key="cbs")
def send_verification_email(email, code):
    """
    Sends a verification email to the specified email address with the provided verification code.

    Parameters:
        email (str): The email address to send the verification email to.
        code (str): The verification code.

    Returns:
        None
    """
    subject = "Mesika CBS Verification Code"
    message = f"Your verification code is: {code}"
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, sender_email, recipient_list)


@shared_task(routing_key="cbs")
def send_password_manager_email(user_id):
    from managers.models import Managers

    try:
        manager = Managers.objects.get(pk=user_id)
    except Managers.DoesNotExist:
        return

    token = default_token_generator.make_token(manager)
    manager.password_reset_token = token
    manager.password_reset_token_created_at = timezone.now()
    manager.save()
    reset_link = f"http://127.0.0.1:8000/staffs/password-reset/confirm/{token}/"
    message = f'Click on the <a href="{reset_link}">link</a> to reset your password.'

    send_mail(
        "Mesika CBS Password Reset",
        message,
        settings.DEFAULT_FROM_EMAIL,
        [manager.email],
        fail_silently=False,
        html_message=message,
    )


@shared_task(routing_key="cbs")
def send_user_password(email, password):
    """
    Sends an email to a user with their password and email address.

    Parameters:
        email (str): The email address of the user.
        password (str): The password of the user.

    Returns:
        None
    """
    subject = "Mesika CBS Credentials"
    link = "https://playpen-control.mesika.org:4443/cbs/"
    message = f"Your account credentials are:\npassword: {password}\nemail: {email}\nlink: {link}"
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, sender_email, recipient_list)


@shared_task(routing_key="cbs")
def send_user_details_after_registration(user):
    from accounts.models import Accounts

    account_number = Accounts.objects.get(user=user['id']).account_number
    subject = "Mesika CBS Registration"
    message = f"Welcome to Mesika CBS, please here are your details:\nFirst name: {user['first_name']}\nLast name: {user['last_name']}\nMobile Number: {user['mobile_number']}\nGhana Card: {user['ghana_card_number']}\nAccount Number:{account_number}"
    sender_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user['email']]
    send_mail(subject, message, sender_email, recipient_list)


@shared_task(routing_key="cbs")
def send_deposit_notification_email(customer_email, amount, balance):
    """Sends a notification email to the customer after they have made a deposit."""

    subject = "Deposit notification"
    body = f"Dear {customer_email},\n\nYou have successfully deposited {amount} into your account. Your new balance is {balance}.\n\nThank you for using our services."

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [customer_email],
        fail_silently=False,
    )


@shared_task(routing_key="cbs")
def send_withdrawal_notification_email(customer_email, amount, balance):
    """Sends a notification email to the customer after they have made a withdrawal."""

    subject = "Withdrawal notification"
    body = f"Dear {customer_email},\n\nYou have successfully withdrawn {amount} from your account. Your new balance is {balance}.\n\nThank you for using our services."

    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [customer_email],
        fail_silently=False,
    )


#################### TWILIO CONFIGURATION ####################

SETTINGS_FILE = os.path.join("config/settings.json")

ALL_SETTINGS = read_config(SETTINGS_FILE)

account_sid = ALL_SETTINGS["twilio"][
    "TWILIO_ACCOUNT_SID"]  # PLACE YOUR ACCOUNT_SID
account_token = ALL_SETTINGS["twilio"]["TWILIO_AUTH_TOKEN"]  # ACCOUNT_TOKEN
sms_from = ALL_SETTINGS["twilio"]["SMS_FROM"]

client = Client(account_sid, account_token)


@shared_task(routing_key="cbs")
def send_verification_code_sms(code, phone_number):
    message = client.messages.create(
        body=f"Hi! Your CSF Verification code is: {code}",
        from_=sms_from,
        to=f"{phone_number}",
    )


@shared_task(routing_key="cbs")
def send_withdrawal_notification_sms(customer_phone_number, amount, balance):
    message = client.messages.create(
        body=f"Dear {customer_phone_number},\n\nYou have successfully withdrawn {amount} from your account. Your new balance is {balance}.\n\nThank you for using our services.",
        from_=sms_from,
        to=f"{customer_phone_number}",
    )


@shared_task(routing_key="cbs")
def send_deposit_notification_sms(customer_phone_number, amount, balance):
    message = client.messages.create(
        body=f"Dear {customer_phone_number},\n\nYou have successfully deposited {amount} into your account. Your new balance is {balance}.\n\nThank you for using our services.",
        from_=sms_from,
        to=f"{customer_phone_number}",
    )


@shared_task(routing_key="cbs")
def send_account_approved_sms(customer_phone_number):
    message = client.messages.create(
        body=f"Dear {customer_phone_number},\n\nYour account has been approved.\n\nThank you for using our services.",
        from_=sms_from,
        to=f"{customer_phone_number}",
    )


@shared_task(routing_key="cbs")
def send_loan_approved_sms(customer_phone_number):
    message = client.messages.create(
        body=f"Dear {customer_phone_number},\n\nYour loan has been approved.\n\nThank you for using our services.",
        from_=sms_from,
        to=f"{customer_phone_number}",
    )


#################### INTEREST RATE CONFIGURATION ####################


@shared_task(routing_key="cbs")
def calculate_interest():
    accounts = Accounts.objects.filter(
        balance__gt=0,
        interest_start_date__gte=timezone.now(),
        initial_deposit_date__isnull=False
    ).select_related('account_type')

    this_month = timezone.now().month

    created_transactions = []
    updated_accounts = []

    for account in accounts:
        if this_month in account.get_interest_calculation_months():
            interest = account.account_type.calculate_interest(
                account.balance
            )
            account.balance += interest
            account.save()

            transaction_obj = Transactions(
                account=account,
                transaction_type=INTEREST,
                amount=interest
            )
            created_transactions.append(transaction_obj)
            updated_accounts.append(account)

    if created_transactions:
        Transactions.objects.bulk_create(created_transactions)

    if updated_accounts:
        Accounts.objects.bulk_update(
            updated_accounts, ['balance']
        )
