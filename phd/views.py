import os

from django.http import JsonResponse
from django.shortcuts import render

from conf.settings import API_KEY
from phd.models import Suz_uzgartiruvchilar,UZB_affiks,Shakil_yasovchi_qushimchalar,Suzlar
import requests
from requests.exceptions import RequestException

import openai
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import TextSerializer

openai.api_key = API_KEY

def imlo_api(text):
    url = "http://213.230.107.46:10006/spelling"
    data = {"text": f"{text}"}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.ConnectionError as ce:
        print(f"ConnectionError: {ce}")
        return None
    except requests.exceptions.Timeout as te:
        print(f"TimeoutError: {te}")
        return None
    except RequestException as e:
        print(f"RequestException: {e}")
        return None



def index(request):
    if request.POST:
        data=imlo_api((request.POST['text']))
        return JsonResponse({'response': data.text})
    else:
        return render(request, 'index.html')

def gramatik_tahrir(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Siz grammatik va uslubiy tahrir qilishda yordam beruvchi yordamchisiz."},
            {"role": "user", "content": f"Quyidagi matnni grammatik va uslubiy jihatdan to'g'rilab bering:\n\n{text}"}
        ],
        temperature=0.7,
    )
    tahrirlangan_matn = response['choices'][0]['message']['content'].strip()
    return tahrirlangan_matn


def tahrir(request):
    if request.POST:
        data=gramatik_tahrir((request.POST['text']))
        return JsonResponse({'response': data})
    return render(request, 'tahrir.html')


class GrammarCorrectionView(APIView):
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']

            openai.api_key = API_KEY
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system",
                     "content": "Siz grammatik va uslubiy tahrir qilishda yordam beruvchi yordamchisiz."},
                    {"role": "user",
                     "content": f"Quyidagi matnni grammatik va uslubiy jihatdan to'g'rilab bering:\n\n{text}"}
                ],
                temperature=0.7,
            )

            tahrirlangan_matn = response['choices'][0]['message']['content'].strip()
            return Response({"corrected_text": tahrirlangan_matn}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)