from django.db import models

# DOCUMENTATION LINK: https://pypi.org/project/whatsapp-api-client-python/
from whatsapp_api_client_python import API

class ManangerWa():
    def send(self, mensage, number):
        greenAPI = API.GreenApi(
            "7103835744", "86c1642f2fdc4a339e847999ed7431dd6ffc2778c4dc4388b6"
        )
        response = greenAPI.sending.sendMessage(f"{number}@c.us", f"{mensage}")
        print(response.data)