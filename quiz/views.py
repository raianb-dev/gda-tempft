import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import requests
from quiz.models import ManangerWa
# Funções auxiliares para detectar bots e dispositivos móveis
def is_mobile_user_agent(user_agent):
    mobile_user_agents = [
        "Mobile", "Android", "iPhone", "iPad", "iPod", "BlackBerry", 
        "Opera Mini", "IEMobile", "Windows Phone"
    ]
    return any(agent in user_agent for agent in mobile_user_agents)


def is_bot_user_agent(user_agent):
    bot_user_agents = [
        'facebookexternalhit', 'TikTokBot', 'Instagram', 
        'Googlebot', 'Bingbot', 'Facebot'
    ]
    return any(bot in user_agent for bot in bot_user_agents)


@csrf_exempt
def init(request):
    # Capturar informações do usuário
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    
    # Detecção de bots
    if is_bot_user_agent(user_agent):
        return render(request,'desktop.html')  # Redireciona para a página de bots

    # Detecção de dispositivos móveis
    if is_mobile_user_agent(user_agent):
        return render(request, 'mobile.html')  # Página específica para dispositivos móveis

    # Redirecionar para usuários desktop
    return render(request, 'desktop.html')  # Página para dispositivos desktop


@csrf_exempt  # Desabilita a verificação CSRF para este endpoint
def webhook_view(request):
    if request.method == 'POST':
        try:
            # Verifica se a requisição possui dados
            if request.body:
                # Carregar os dados JSON do corpo da requisição
                data = json.loads(request.body.decode('utf-8'))
            else:
                print("Nenhum dado foi recebido.")  # Caso não haja dados na requisição
            mobile_number = data.get('Customer', {}).get('mobile', None)
            mobile_number = mobile_number.replace('+', '')
            
            # Remove o "9" extra apenas se for após o código do país (55) e o DDD (2 dígitos)
            mobile_number = re.sub(r'^(55\d{2})9(\d{8})$', r'\1\2', mobile_number)
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
            ManangerWa.send(ManangerWa,message, mobile_number)
            url = "https://7103.media.greenapi.com/waInstance7103835744/sendFileByUpload/86c1642f2fdc4a339e847999ed7431dd6ffc2778c4dc4388b6"

            payload = {
            'chatId': f'{mobile_number}@c.us', 
            'fileName': 'ACESSO VISION RAIO-X'
            }
            files = [
            ('file', ('ACESSO VISION RAIO-X.pdf', open('ACESSO VISION RAIO-X.pdf','rb'),'application/pdf'))
            ]
            response = requests.post(url, data=payload, files=files)

            print(response.text.encode('utf8'))
            # Responder com sucesso
            return JsonResponse({"status": "success", "message": "Webhook recebido com sucesso!"}, status=200)
        
        except json.JSONDecodeError as e:
            print("Erro ao processar JSON:", e)  # Log do erro
            return JsonResponse({"status": "error", "message": "Erro ao processar os dados."}, status=400)
    
    # Método não permitido
    return JsonResponse({"status": "error", "message": "Método não permitido."}, status=405)