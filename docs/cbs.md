# CORE BANKING SYSTEM

This document describes the **CORE BANKING SYSTEM** in detail.

## Customer Creation
### Method: POST
### Path: /customers/create-customer
### Token: Required

### Form Data:
| Name                   | Type   | Description                      | Required |
|------------------------|--------|----------------------------------|----------|
| email                  | string | Email of the customer            | Yes      |
| account_type           | string | Account type of the customer     | Yes      |
| first_name             | string | First name of the customer       | Yes      |
| last_name              | string | Last name of the customer        | Yes      |
| sex                    | string | Gender of the customer           | Yes      |
| occupation             | string | Customer's occupation            | Yes      |
| mobile_number          | string | Phone number of the customer     | Yes      |
| ghana_card_number      | string | Ghana card number of the customer| Yes      |
| date_of_birth          | string | Date of birth of the customer    | Yes      |
| city                   | string | City of residence                | Yes      |
| postal_address         | string | Postal address                   | Yes      |
| marital_status         | string | Marital status of the customer   | Yes      |
| next_of_kin_name       | string | Name of the next of kin          | Yes      |
| next_of_kin_phone_number| string | Phone number of the next of kin  | Yes      |
| next_of_kin_address    | string | Address of the next of kin       | Yes      |
| next_of_kin_relationship| string | Relationship with the next of kin| Yes      |
| image                  | file   | Customer's image                 | Yes      |

### Response:
```json
{
  "message": "User created successfully",
  "status": 200,
  "data": {
    "profile_id": "ufyu1609",
    "email": "user2@gmail.com",
    "first_name": "Dominic",
    "last_name": "Kofi",
    "ghana_card_number": "GH-2247476734",
    "mobile_number": "+23357837434",
    "occupation": "Engineer",
    "date_of_birth": "2000-04-20",
    "city": "Accra",
    "postal_address": "AC-056335",
    "sex": "MALE",
    "marital_status": "SINGLE",
    "next_of_kin_name": "Ben",
    "next_of_kin_phone_number": "0237683493",
    "next_of_kin_address": "Kumasi",
    "next_of_kin_relationship": "Brother",
    "account_type": "Checking Account",
    "account_number": "AB-9560368921",
    "image": "/media/uploads/customers/0642e9e6-d7c5-440d-ad19-55a3fe386beb.png"
  }
}
```

## Staff Login
### Method: POST
### Path: /staffs/login

### Request Body:
| Name     | Type   | Description             | Required |
| -------- | ------ | ----------------------- | -------- |
| email    | string | Email of the staff      | Required |
| password | string | Password for the staff   | Required |


### Response:
```json
{
  "message": "Please check your email for the verification code.",
  "status": 200,
  "data": {
    "profile_id": "cgqn8822",
    "email": "it_manager@gmail.com",
    "first_name": "Dominic",
    "last_name": "IT",
    "staff_id": "AT2023",
    "phone_number": "023456789",
    "roles": [
      "IT_MANAGER"
    ],
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xNjk1NDcxMzIwf"
  }
}
```

## Staff OTP Verification
### Method: POST
### Path: /staffs/otp-verification
### Token: Required

### Request Body:
| Name | Type   | Description            | Required |
| ---- | ------ | ----------------------  | -------- |
| otp  | string | OTP for verification    | Required |


### Response:
```json
{
  "message": "OTP verified for it_manager@gmail.com. User logged in.",
  "status": 200,
  "data": {
    "profile_id": "cgqn8822",
    "email": "it_manager@gmail.com",
    "first_name": "Dominic",
    "last_name": "IT",
    "staff_id": "AT2023",
    "phone_number": "023456789",
    "roles": [
      "IT_MANAGER"
    ],
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c"
  }
}
```

## Staff Password Reset
### Method: POST
### Path: /staffs/password-reset

### Request Body:
| Name  | Type   | Description         | Required |
| ----- | ------ | ------------------- | -------- |
| email | string | Email for reset     | Required |


### Response:
```json
{
  "message": "Password reset email sent to teller@gmail.com.",
  "status": 200
}
```


## Staffs
### Method: GET
### Path: /staffs/staffs
### Token: Required

### Response:
```json
{
  "message": "Staff listed successfully",
  "status": 200,
  "current_page": 1,
  "total_pages": 1,
  "data": [
    {
      "profile_id": "gntc7110",
      "email": "customer_service@gmail.com",
      "first_name": "Bruce",
      "last_name": "Cutomer Service",
      "phone_number": "0234567339",
      "staff_id": "TE20288",
      "roles": "CUSTOMER_SERVICE"
    },
    {
      "profile_id": "hwmd4115",
      "email": "manager@gmail.com",
      "first_name": "Bruce",
      "last_name": "Manager",
      "phone_number": "0234567333",
      "staff_id": "TE20286",
      "roles": "MANAGER"
    }, 
    ]
}
```

## Staff Details
### Method: POST
### Path: /staffs/staff-details
### Token: Required

### Request Body:
| Name        | Type   | Description        | Required |
| ----------- | ------ | ------------------ | -------- |
| profile_id  | string | Profile ID of staff | Required |


### Response
```json
{
  "message": "Staff details found",
  "status": 200,
  "data": {
    "profile_id": "cgqn8822",
    "email": "it_manager@gmail.com",
    "first_name": "Dominic",
    "last_name": "IT",
    "staff_id": "AT2023",
    "phone_number": "023456789",
    "roles": [
      "IT_MANAGER"
    ]
  }
}
```

## Roles
### Method: GET
### Path: /staffs/roles
### Token: Required

### Response:
```json
{
  "message": "Roles listed sucessfully",
  "status": 200,
  "data": [
    {
      "id": 1,
      "name": "IT_MANAGER"
    },
    {
      "id": 2,
      "name": "MANAGER"
    },
    {
      "id": 3,
      "name": "TELLER"
    }
  ]
}
```


## Customers
### Method: GET
### Path: /customers/list-customers
### Token: Required

### Response:
```json
{
  "message": "customers listed successfully",
  "status": 200,
  "current_page": 1,
  "total_pages": 1,
  "data": [
    {
      "profile_id": "wkys9053",
      "email": "customer@gmail.com",
      "first_name": "Dominic",
      "last_name": "Bruce",
      "mobile_number": "0246789877",
      "city": "Accra",
      "account_number": "MC-7756293440",
      "amount": 280,
      "is_approved": "PENDING"
    }
  ]
}
```

## Customer Details
### Method: POST
### Path: /customers/customer-details
### Token: Required

### Request Body:
| Name            | Type   | Description                | Required |
| --------------- | ------ | -------------------------- | -------- |
| account_number  | string | Account number of customer | Required |


### Response:
```json
{
  "message": "Customer details found",
  "status": 200,
  "data": {
    "profile_id": "zbgw0918",
    "balance": "100.00",
    "email": "user@gmail.com",
    "first_name": "Dominic",
    "last_name": "Bruce",
    "ghana_card_number": "GH-02986599",
    "phone_number": "0246789877",
    "occupation": "Engineer",
    "date_of_birth": "2000-04-20",
    "city": "Accra",
    "postal_address": "AC-056335",
    "sex": "MALE",
    "marital_status": "SINGLE",
    "account_number": "SK-3008543580",
    "next_of_kin_name": "Ben",
    "next_of_kin_phone_number": "0234567",
    "next_of_kin_address": "Accra",
    "next_of_kin_relationship": "Brother"
  }
}
```

## Token Verification
### Method: POST
### Path: /staffs/verify-token
### Token: Required

### Request Body:
| Name  | Type   | Description               | Required |
| ----- | ------ | ------------------------- | -------- |
| token | string | Token for verification    | Required |


### Response:
```json
{
  "message": "Token verified",
  "status": 200,
  "data": {
    "profile_id": "dxln3570",
    "email": "teller@gmail.com",
    "first_name": "Dominic",
    "last_name": "Teller",
    "staff_id": "TE2023",
    "phone_number": "023456789",
    "roles": [
      "TELLER"
    ]
  }
}
```

## Transaction (Deposit)
### Method: POST
### Path: /transactions/deposit/
### Token: Required

### Request Body:
| Name            | Type    | Description                          | Required |
| --------------- | ------- | ------------------------------------ | -------- |
| amount          | number  | Amount for the transaction           | Required |
| account_number  | string  | Account number for the transaction   | Required |
| narration       | string  | Transaction narration (optional)     | Optional  |


### Response:
```json
{
  "message": "Transaction created successfully for EM-2552460091 account for 50 amount",
  "status": 200
}
```

## Transactions 
### Method: GET
### Path: /transactions/transactions
### Token: Required

### Response:
```json
{
  "message": "transactions listed successfully",
  "status": 200,
  "current_page": 1,
  "total_pages": 1,
  "data": [
    {
      "first_name": "Dominic",
      "last_name": "Bruce",
      "amount": 100,
      "account_number": "MC-7756293440",
      "date_created": "2023-10-13",
      "transaction_type": "deposit",
      "reference_number": "DB-9411"
    },
    {
      "first_name": "Dominic",
      "last_name": "Bruce",
      "amount": 5,
      "account_number": "MC-7756293440",
      "date_created": "2023-10-13",
      "transaction_type": "withdrawal",
      "reference_number": "DB-1280"
    }
  ]
}
```

## Transaction (Withdrawal)
### Method: POST
### Path: /transactions/withdrawal/
### Token: Required

### Request Body:
| Name            | Type    | Description                          | Required |
| --------------- | ------- | ------------------------------------ | -------- |
| amount          | number  | Amount for the transaction           | Required |
| account_number  | string  | Account number for the transaction   | Required |
| narration       | string  | Transaction narration (optional)     | Optional  |


### Response:
```json
{
  "message": "Transaction created successfully for EM-2552460091 account for 50 amount",
  "status": 200
}
```

## Accounts
### Method: GET
### Path: /accounts/accounts
### Token: Required

### Response:
```json
{
  "message": "Accounts listed successfully",
  "status": 200,
  "current_page": 1,
  "total_pages": 1,
  "data": [
    {
      "balance": "100.00",
      "account_number": "SK-3008543580",
      "date_created": "2023-10-25T14:46:43.449Z",
      "first_name": "Dominic",
      "last_name": "Bruce"
    }
  ]
}
```

## Deposit Between Accounts
### Method: POST
### Path: /transactions/deposit-between-accounts
### Token: Required

### Request Body:
| Name                | Type   | Description                             | Required |
| ------------------- | ------ | --------------------------------------- | -------- |
| amount              | number | Amount to be transferred                | Required |
| from_account_number | string | Source account number                   | Required |
| to_account_number   | string | Destination account number              | Required |


### Response:
```json
{
    "message": "Transaction created successfully from account SK-3008543580 to account AB-9560368921 for 100 amount",
    "status": 200
}
```


## Update Customer
### Method: POST
### Path: /customers/update-customer/{profile_id}/
### Token: Required

### Request Body:
| Name                    | Type    | Description                           | Required |
| ----------------------- | ------- | ------------------------------------- | -------- |
| email                   | string  | Email of the customer                 | Required |
| account_number          | string  | Account number of the customer        | Required |
| mobile_number           | string  | Phone number of the customer          | Required |
| occupation              | string  | Customer's occupation                 | Required |
| first_name              | string  | First name of the customer            | Required |
| last_name               | string  | Last name of the customer             | Required |
| ghana_card_number       | string  | Ghana card number of the customer     | Required |
| date_of_birth           | string  | Date of birth of the customer         | Required |
| city                    | string  | City of residence                     | Required |
| postal_address          | string  | Postal address                        | Required |
| sex                     | string  | Gender of the customer                | Required |
| marital_status          | string  | Marital status of the customer        | Required |
| next_of_kin_name        | string  | Name of the next of kin               | Required |
| next_of_kin_phone_number| string  | Phone number of the next of kin       | Required |
| next_of_kin_address     | string  | Address of the next of kin            | Required |
| next_of_kin_relationship | string  | Relationship with the next of kin     | Required |


### Response:
```json
{
  "message": "Customer profile updated successfully",
  "status": 200,
  "data": {
    "profile_id": "mxrn0745",
    "account_number": "SA-4011067563",
    "email": "diana@gmail.com",
    "first_name": "John",
    "last_name": "Doe",
    "ghana_card_number": "GH-2234567890",
    "mobile_number": "5655555555",
    "occupation": "Engineer",
    "date_of_birth": "1990-01-01",
    "city": "Accra",
    "postal_address": "123 Main Street",
    "sex": "Female",
    "marital_status": "Single",
    "next_of_kin_name": "Jane Doe",
    "next_of_kin_phone_number": "987654321",
    "next_of_kin_address": "456 Elm Street",
    "next_of_kin_relationship": "Sibling"
  }
}
```


## Update Customer Status (Approve Account)
### Method: POST
### Path: /customers/update-status/{profile_id}/
### Token: Required

### Request Body:
| Name   | Type   | Description                           | Required |
| ------ | ------ | ------------------------------------- | -------- |
| status | string | Updated status of the customer        | Required |


### Response:
```json
{
  "message": "Customer status updated successfully",
  "status": 200,
  "data": {
    "profile_id": "vueq5489",
    "email": "customer@gmail.com",
    "first_name": "Dominic",
    "last_name": "Bruce",
    "ghana_card_number": "GH-0986599",
    "mobile_number": "0246789876",
    "occupation": "Engineer",
    "date_of_birth": "2000-04-20",
    "city": "Accra",
    "postal_address": "AC-056335",
    "sex": "MALE",
    "marital_status": "SINGLE",
    "next_of_kin_name": "Ben",
    "next_of_kin_phone_number": "0234567",
    "next_of_kin_address": "Accra",
    "next_of_kin_relationship": "Brother"
  }
}
```


## Account Types
### Method: GET
### Path: /accounts/account-types
### Token: Required

### Response:
```json
{
  "message": "Account types listed sucessfully",
  "status": 200,
  "data": [
    {
      "id": 1,
      "account_type": "Checking Account"
    },
    {
      "id": 2,
      "account_type": "Certificate of Deposit (CD)"
    },
    {
      "id": 3,
      "account_type": "Savings Account"
    },
    {
      "id": 4,
      "account_type": "Money Market Account (MMA)"
    }
  ]
}
```


## Create Loan
### Method: POST
### Path: /loans/create-loan
### Token: Required

### Request Body:
| Name               | Type    | Description                  | Required |
| ------------------ | ------- | ---------------------------- | -------- |
| ghana_card_number  | string  | Ghana card number            | Required |
| amount             | number  | Loan amount                  | Required |
| loan_type          | number  | Type of loan                 | Required |


### Response:
```json
{
  "message": "Loan created successfully",
  "status": 200,
  "data": {
    "profile_id": "zbgw0918",
    "first_name": "Dominic",
    "last_name": "Bruce",
    "ghana_card_number": "GH-02986599",
    "mobile_number": "0246789877",
    "amount": 5000,
    "interest_amount": "150.00",
    "amount_to_pay": "5150.00",
    "date_applied": "2023-10-25T15:00:55.336Z",
    "loan_type": "Peronal loans"
  }
}
```


## Loans
### Method: GET
### Path: /loans/list-loans
### Token: Required

### Response:
```json
{
  "message": "loans listed successfully",
  "status": 200,
  "data": [
    {
      "id": 2,
      "borrower__first_name": "Dominic",
      "borrower__last_name": "Bruce",
      "borrower__ghana_card_number": "GH-02986599",
      "borrower__mobile_number": "0246789877",
      "amount": "5000.00",
      "loan_type__name": "Peronal loans",
      "interest_amount": "150.00",
      "amount_to_pay": "5150.00",
      "date_applied": "2023-10-25T14:58:56.943Z",
      "approved": false
    }
  ]
}
```

## Loan Details
### Method: POST
### Path: /loans/loan-details
### Token: Required

### Request Body:
| Name               | Type   | Description            | Required |
| ------------------ | ------ | ---------------------- | -------- |
| ghana_card_number  | string | Ghana card number      | Required |


### Response:
```json
{
  "message": "Loan details found",
  "status": 200,
  "data": {
    "ghana_card_number": "GH-02986599",
    "mobile_number": "0246789877",
    "first_name": "Dominic",
    "last_name": "Bruce",
    "loan_amount": "5000.00",
    "interest_amount": "845.53",
    "amount_to_pay": "5845.53",
    "total_repaid": "50",
    "amount_remaining": "5795.53",
    "date_applied": "2023-10-13T14:30:30.465Z"
  }
}
```

## Approve Loan
### Method: POST
### Path: /loans/approve-loan/{id}/
### Token: Required

### Request Body:
| Name   | Type   | Description         | Required |
| ------ | ------ | ------------------- | -------- |
| status | boolean| Loan approval status| Required |


### Response:
```json
{
  "message": "Loan status updated successfully",
  "status": 200,
  "data": {
    "profile_id": "vueq5489",
    "first_name": "Dominic",
    "last_name": "Bruce",
    "ghana_card_number": "GH-0986599",
    "mobile_number": "+233542674431"
  }
}
```

## Check Loan Payment Status
### Method: GET
### Path: /loans/has-finished-payment/{id}/
### Token: Required

This command is a GET request to the '/loans/has-finished-payment/8/' endpoint. It is used to check if a specific loan (in this case, with ID 8) has finished its payment or not.

### Response:
```json
{
  "message": "Loan has not been fully paid",
  "status": 200,
  "data": {
    "profile_id": "wkys9053",
    "first_name": "Dominic",
    "last_name": "Bruce",
    "ghana_card_number": "GH-02986599",
    "mobile_number": "0246789877",
    "loan_amount": "5000.00",
    "amount_to_pay": "5845.53",
    "amount_remaining": "5845.53",
  }
}
```

## Loan Repayment
### Method: POST
### Path: /loans/loan-repayment
### Token: Required

### Request Body:
| Name               | Type   | Description                 | Required |
| ------------------ | ------ | --------------------------- | -------- |
| ghana_card_number  | string | Ghana card number           | Required |
| amount             | number | Repayment amount            | Required |


### Response:
```json
{
  "message": "Repayment created successfully",
  "status": 200,
  "data": {
    "ghana_card_number": "GH-0986599",
    "amount": 50
  }
}
```

## Transactions by Type Search
### Method: GET
### Path: /transactions/transactions-by-search/?type=withdrawal
### Token: Required
### Query Parameters:
| Name   | Type   | Description         | Required |
| ------ | ------ | ------------------- | -------- |
| type   | string | Transaction type    | Required |

This is a GET request to the '/transactions/transactions-by-search/' endpoint, specifically filtering transactions by the 'withdrawal or deposit' type. It fetches a list of transactions based on the specified type through the query parameter.


### Response:
```json
{
  "message": "Transactions listed successfully",
  "status": 200,
  "data": [
    {
      "user__first_name": "Dominic",
      "user__last_name": "Bruce",
      "amount": 5,
      "account_number": "MC-7756293440",
      "date_created": "2023-10-13T09:16:21.374Z",
      "transaction_type": "withdrawal",
      "reference_number": "DB-2365"
    },
    {
      "user__first_name": "Dominic",
      "user__last_name": "Bruce",
      "amount": 5,
      "account_number": "MC-7756293440",
      "date_created": "2023-10-13T09:16:38.553Z",
      "transaction_type": "withdrawal",
      "reference_number": "DB-3027"
    }
  ]
}
```

## Transaction Statement by Type and Account Number
### Method: GET
### Path: /transactions/transaction-statement/?type=withdrawal&account_number=MC-7756293440
### Token: Required
### Query Paramerters:
| Name   | Type   | Description         | Required |
| ------ | ------ | ------------------- | -------- |
| type   | string | Transaction type    | Required |
| account_number | string | Account number     | Optional |
|date | string | Date           | Optional |

This is a GET request to the '/transactions/transaction-statement/' endpoint, aiming to fetch a transaction statement filtered by the 'withdrawal' type and specific 'account_number' (MC-7756293440). It retrieves a statement of transactions for the specified account and type.


## Loan Types
### Method: GET
### Path: /loans/list-loan-types
### Token: Required

### Response:
```json
{
  "message": "Loan Types listed successfully",
  "status": 200,
  "data": [
    {
      "id": 1,
      "name": "Personal Loan"
    },
    {
      "id": 2,
      "name": "Business Loan"
    },
    {
      "id": 3,
      "name": "Car Loan"
    }
  ]
}
```

## Create Loan Type
### Method: POST
### Path: /loans/create-loan-type
### Token: Required

### Request Body:
| Name                          | Type    | Description                          | Required |
| ----------------------------- | ------- | ------------------------------------ | -------- |
| name                          | string  | Name of the loan type                | Required |
| annual_interest_rate          | integer | Annual interest rate (0-100)         | Required |
| interest_calculation_per_year | integer | Number of interest calculations/year | Required |


### Response:
```json
{
  "message": "Loan type created successfully",
  "status": 200,
  "data": {
    "id": 6,
    "name": "Church Loans",
    "annual_interest_rate": 1,
    "interest_calculation_per_year": 1
  }
}
```

## Update Loan Type
### Method: POST
### Path: /loans/update-loan-type/{id}
### Token: Required

### Request Body:
| Name                          | Type    | Description                          | Required |
| ----------------------------- | ------- | ------------------------------------ | -------- |
| name                          | string  | Name of the loan type                | Required |
| annual_interest_rate          | integer | Annual interest rate (0-100)         | Required |
| interest_calculation_per_year | integer | Number of interest calculations/year | Required |


 ### Response:
```json
{
  "message": "Loan type updated successfully",
  "status": 200,
  "data": {
    "id": 6,
    "name": "Church Loans",
    "annual_interest_rate": 1,
    "interest_calculation_per_year": 1
  }
}
```

## Create Account Type
### Method: POST
### Path: /accounts/create-account-type
### Token: Required

### Request Body:
| Name                          | Type    | Description                           | Required |
| ----------------------------- | ------- | ------------------------------------- | -------- |
| account_type                  | string  | Type of the account                   | Required |
| maximum_withdrawal_amount     | number  | Maximum withdrawal amount              | Required |
| annual_interest_rate          | number  | Annual interest rate                  | Required |
| interest_calculation_per_year | number  | Number of interest calculations/year  | Required |


### Response:
```json
{
  "message": "Account type created successfully",
  "status": 200,
  "data": {
    "id": 5,
    "account_type": "Savings",
    "maximum_withdrawal_amount": 10000,
    "annual_interest_rate": 2.5,
    "interest_calculation_per_year": 12
  }
}
```

## Update Account Type
### Method: POST
### Path: /accounts/update-account-type/{id}
### Token: Required

### Request Body:
| Name                          | Type    | Description                           | Required |
| ----------------------------- | ------- | ------------------------------------- | -------- |
| account_type                  | string  | Type of the account                   | Required |
| maximum_withdrawal_amount     | number  | Maximum withdrawal amount              | Required |
| annual_interest_rate          | number  | Annual interest rate                  | Required |
| interest_calculation_per_year | number  | Number of interest calculations/year  | Required |


 ### Response:
```json
{
  "message": "Account type updated successfully",
  "status": 200,
  "data": {
    "id": 5,
    "account_type": "Savings",
    "maximum_withdrawal_amount": 10000,
    "annual_interest_rate": 2.5,
    "interest_calculation_per_year": 12
  }
}
```



## Verify Account Number
### Method: POST
### Path: /account/verify-account-number/
### Token: Required


### Request Body:
| Name                          | Type    | Description                           | Required |
| ----------------------------- | ------- | ------------------------------------- | -------- |
| account_number                | string  | Type of the account                   | Required |


### Response
```json
{
  "message": "Account verified successfully",
  "status": 200,
  "data": {
    "account_number": "DZ-0588272442",
    "account_type": "Checking Account",
    "first_name": "Dominic",
    "last_name": "Kofi",
    "email": "user1@gmail.com",
    "mobile_number": "+23357837434"
  }
}
```



## Linked Account
### Method: POST
### Path: /account/linked-accounts/
### Token: Required


### Request Body:
| Name                          | Type    | Description                           | Required |
| ----------------------------- | ------- | ------------------------------------- | -------- |
| customer_ghana_card           | string  | Customer Ghana Card Number            | Required |


### Response
```json
{
  "message": "Account data listed successfully",
  "status": 200,
  "data": [
    {
      "account_number": "DZ-0588272442",
      "account_type": "Checking Account",
      "first_name": "Dominic",
      "last_name": "Kofi",
      "email": "user1@gmail.com",
      "mobile_number": "+23357837434"
    },
    {
      "account_number": "NA-5799223862",
      "account_type": "Savings Account",
      "first_name": "Dominic",
      "last_name": "Kofi",
      "email": "user1@gmail.com",
      "mobile_number": "+23357837434"
    }
  ]
}
```




## Add Money To Vault
### Method: POST
### Path: /transaction/add-money-to-vault/
### Token: Required


### Request Body:
| Name                          | Type    | Description                           | Required |
| ----------------------------- | ------- | ------------------------------------- | -------- |
| amount                        | Decimal | Amount to put into the vault          | Required |


### Response
```json
{
  "message": "Amount added to vault successfully",
  "status": 200
}
```


## Vaults
### Method: GET
### Path: /transaction/vaults/
### Token: Required


### Request Body:
| Name                          | Type    | Description                           | Required |
| ----------------------------- | ------- | ------------------------------------- | -------- |
| amount                        | Decimal | Amount to put into the vault          | Required |


### Response
```json
{
  "message": "Teller vaults listed successfully",
  "status": 200,
  "data": [
    {
      "id": 2,
      "staff_id": "TE20294",
      "amount": "20000.00"
    },
    {
      "id": 3,
      "staff_id": "TE20294",
      "amount": "50000.00"
    },
    {
      "id": 4,
      "staff_id": "TE20292",
      "amount": "50000.00"
    }
  ]
}
```


## Assign Vault To Teller
### Method: POST
### Path: /transaction/assign-vault-to-teller/
### Token: Required


### Request Body:
| Name                          | Type    | Description                           | Required |
| ----------------------------- | ------- | ------------------------------------- | -------- |
| staff_id                      | String  | Staff ID                              | Required |
| vault_id                      | Digit   | Vault ID                              | Required |

### Response
```json
{
  "message": "Teller assigned to the vault successfully",
  "status": 200,
  "data": {
    "teller_vault_id": 2,
    "teller_name": "Dominic Teller",
    "vault_amount": "20000.00"
  }
}
```