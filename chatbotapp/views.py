from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .chatbot import chatbot


def home(request):
    return render(request, 'chatbotapp/index.html')


@csrf_exempt  # Temporairement pour tester sans CSRF
def get_response(request):
    if request.method == 'POST':
        try:
            # Méthode 1: avec json.loads
            data = json.loads(request.body.decode('utf-8'))
            user_message = data.get('message', '')

            # Méthode alternative: avec request.POST
            # user_message = request.POST.get('message', '')

            print(f"Message reçu: {user_message}")  # Debug

            if user_message:
                bot_response = chatbot.get_response(user_message)
                return JsonResponse({'response': bot_response})
            else:
                return JsonResponse({'response': 'Message vide reçu'})

        except json.JSONDecodeError:
            return JsonResponse({'response': 'Erreur: JSON invalide'}, status=400)
        except Exception as e:
            print(f"Erreur: {e}")  # Debug
            return JsonResponse({'response': f'Erreur interne: {str(e)}'}, status=500)

    return JsonResponse({'response': 'Méthode non autorisée. Utilisez POST.'}, status=405)