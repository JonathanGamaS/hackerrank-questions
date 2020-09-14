body = {
    "ERROR": "false",
    "message": "Sucesso",
    "data": {
        "payment": {
            "hash": "5f5fb033a5d2dba5d5252ad013db54b8d18e7623d9c33fe8",
            "pin": "942252515",
            "country": "br",
            "merchant_payment_code": "2662854444",
            "order_number": "null",
            "status": "CO",
            "status_date": "2020-09-14 18:02:26",
            "open_date": "2020-09-14 18:02:26",
            "confirm_date": "2020-09-14 18:02:26",
            "transfer_date": "null",
            "amount_br": "4117.49",
            "amount_ext": "4117.49",
            "amount_iof": "0.00",
            "currency_rate": "1.0000",
            "currency_ext": "BRL",
            "due_date": "2020-09-17",
            "instalments": "4",
            "payment_type_code": "visa",
            "details": {
                "billing_descriptor": "EBANX*E PECA"
            },
            "transaction_status": {
                "acquirer": "EBANX",
                "code": "OK",
                "description": "Accepted",
                "authcode": "83849"
            },
            "pre_approved": "true",
            "capture_available": "false",
            "split": [
                {
                    "recipient_code": "The One Harley-Davidson - Curitiba/PR",
                    "liable": "true",
                    "charge_fee": "true",
                    "amount": 2210.36
                },
                {
                    "recipient_code": "Red Wheel Harley-Davidson - Londrina/PR",
                    "liable": "true",
                    "charge_fee": "true",
                    "amount": 460.6
                },
                {
                    "recipient_code": "Cascavel Harley-Davidson - Cascavel/PR",
                    "liable": "true",
                    "charge_fee": "true",
                    "amount": 1446.53
                }
            ]
        },
        "status": "SUCCESS"
    }
}

def verificando_onde_esta_status(body):
    status = body["data"]["status"]
    print(status)
    return status

verificando_onde_esta_status(body)