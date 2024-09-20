from django.shortcuts import render, redirect
from .forms import AiForm, UserRegisterForm
import json
import requests



def home(req):
    return render(req, 'homepage.html')


def Ai(req):
    if req.method == 'POST':
        feed = AiForm(req.POST)

        if feed.is_valid():
            daot = feed.cleaned_data['text']
            headers = {
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzZlMzU1MTEtNWJkOS00NTJhLWJhZTItNjVhYmUyOTlkYWQ1IiwidHlwZSI6ImFwaV90b2tlbiJ9.WWuetsdB45bz5akhOlAQtVc-9sFtmtMD3qZRmS3s1r0"}

            url = "https://api.edenai.run/v2/image/generation"
            payload = {
                "providers": "openai/dall-e-3",
                "text": daot,
                "resolution": "1024x1024",
            }

            response = requests.post(url, json=payload, headers=headers)
            result = json.loads(response.text)
            response = result['openai/dall-e-3']['items'][0]['image_resource_url']

            return render(req,'form.html', {'feed': feed, 'response': response})
    else:
        feed = AiForm()

        return render(req, 'form.html', {'feed': feed})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


