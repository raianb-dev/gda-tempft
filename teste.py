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
        
message = """
🎉 Parabéns por adquirir o Método Vision Raio-X! 🎉

Agora você tem acesso exclusivo a uma ferramenta incrível. Siga os passos abaixo para começar:

1️⃣ Crie sua conta no site: porngen.art/undress-ai
👉 Após criar sua conta, você poderá carregar a imagem que deseja editar de forma simples e prática.

2️⃣ Acesso ilimitado!
Com o Vision Raio-X, você terá acesso exclusivo para criar contas ilimitadas com este link especial.
📌 Cada conta inclui 100 créditos diários para utilizar todas as funcionalidades da ferramenta!

3️⃣ Fácil e direto:
Não é necessário criar conta em outras plataformas ou no local onde adquiriu o método.

4️⃣ Acesse rapidamente:
O Vision Raio-X pode ser acessado diretamente pelo WhatsApp e através do documento explicativo (Google Docs) que será enviado para você em instantes.

💡 Dúvidas ou suporte?
📧 Entre em contato pelo nosso e-mail oficial:
z3-contato@live.com

Explore o Vision Raio-X e descubra um mundo de possibilidades! 🚀
"""
ManangerWa.send(ManangerWa, message, "556392180353")
import requests

url = "https://7103.media.greenapi.com/waInstance7103835744/sendFileByUpload/86c1642f2fdc4a339e847999ed7431dd6ffc2778c4dc4388b6"

payload = {
'chatId': '556392180353@c.us', 
'fileName': 'ACESSO VISION RAIO-X'
}
files = [
('file', ('ACESSO VISION RAIO-X.pdf', open('ACESSO VISION RAIO-X.pdf','rb'),'application/pdf'))
]
headers= {}

response = requests.post(url, data=payload, files=files)

print(response.text.encode('utf8'))