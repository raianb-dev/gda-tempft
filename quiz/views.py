import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

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
            # Carregar os dados JSON do corpo da requisição
            data = json.loads(request.body.decode('utf-8'))
            
            # Processar os dados (exemplo)
            # Aqui você pode realizar ações como salvar no banco, fazer chamadas externas, etc.
            print(data)
            
            # Responder com sucesso
            return JsonResponse({"status": "success", "message": "Webhook recebido com sucesso!"}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Erro ao processar os dados."}, status=400)
    
    return JsonResponse({"status": "error", "message": "Método não permitido."}, status=405)