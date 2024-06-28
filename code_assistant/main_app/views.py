import os
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
import openai
import logging

logger = logging.getLogger(__name__)

# Utiliser la clé API depuis les paramètres
openai.api_key = settings.OPENAI_API_KEY

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def generate_snippet_form(request):
    return render(request, 'generate_snippet.html')

def generate_snippet(request):
    if request.method == 'POST':
        description = request.POST.get('description', '')
        language = request.POST.get('language', '')

        if not description or not language:
            logger.error("Description or language not provided")
            return JsonResponse({'error': 'Description or language not provided'}, status=400)

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Generate a {language} code snippet for: {description}"}
                ]
            )

            snippet = response.choices[0].message['content'].strip()
            logger.debug(f"Generated snippet: {snippet}")
            return JsonResponse({'snippet': snippet})
        except openai.error.OpenAIError as e:
            error_message = str(e)
            if "quota" in error_message.lower():
                logger.error(f"Quota reached: {error_message}")
                return JsonResponse({'error': 'Quota reached. Please try again later or upgrade your plan.'}, status=429)
            else:
                logger.error(f"OpenAIError: {error_message}")
                return JsonResponse({'error': error_message}, status=500)
    else:
        logger.error("Invalid request method")
        return JsonResponse({'error': 'Invalid request method'}, status=405)
