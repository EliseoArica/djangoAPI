from culqi.client import Culqi

"""

culqi = Culqi(public_key="pk_test_b8a5e9e9bc9b4fc6", private_key="sk_test_3029fd88f13f8766")

response = culqi.charge.create({
    "amount": 1000,
    "currency_code": "PEN",
    "description": "Venta de prueba",
    "email": "test@gmail.com",
    "source_id": "tkn_test_0jOEnKPuTYA4yiB7",
})

print(response["data"])

"""

def generar_cargo(data):
    culqi = Culqi(public_key="pk_test_b8a5e9e9bc9b4fc6", private_key="sk_test_3029fd88f13f8766")
    response = culqi.charge.create(data)
    return response["status"]
