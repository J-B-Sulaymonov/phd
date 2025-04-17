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

# def gramatik_tahrir(text):
#     response = openai.ChatCompletion.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "Siz grammatik va uslubiy tahrir qilishda yordam beruvchi yordamchisiz."},
#             {"role": "user",
#              "content": f"Quyidagi matndagi so‘zlarning grammatik va imloviy xatolarini to‘g‘irlang, masalan: 'maytab' so‘zi 'maktab' ga. Matndagi mavjud so‘zlar o‘zgartirilishi mumkin, lekin yangi so‘zlar qo‘shilmasin. Matnda qisqartirib yozilgan so‘zlar to‘g‘irlansin. Matnning birinchi harfi katta harf bilan boshlanishi kerak. \n\n{text}"}
#             # {"role": "user", "content": f"Quyidagi matndagi so'zlarning xatosini to'g'rilab bering, matnga qo'shimcha so'zlar qo'shilmasin, matndagi birinchi harf katta bo'lsin: \n\n{text}"} # bn, bilan
#             # {"role": "user", "content": f"Quyidagi matnni grammatik va uslubiy jihatdan to'g'rilab bering:\n\n{text}"} # optimal
#         ],
#         # messages=[
#         #     {"role": "system", "content": "Siz grammatik va uslubiy tahrir qilishda yordam beruvchi yordamchisiz."},
#         #     {"role": "user", "content": f"Quyidagi matnni grammatik va uslubiy jihatdan to'g'rilab bering:\n\n{text}"}
#         # ],
#         temperature=0.7,
#     )
#     tahrirlangan_matn = response['choices'][0]['message']['content'].strip()
#     return tahrirlangan_matn

# from langdetect import detect
# def tahrir(request):
#     if request.POST:
#         if len(request.POST['text'])>10:
#             detected_lang = detect(request.POST['text'])
#             print(detected_lang)
#             if detected_lang != "en" and detected_lang != 'ru':
#                 if request.POST:
#                     data=gramatik_tahrir((request.POST['text']))
#                     return JsonResponse({'response': data})
#     return render(request, 'tahrir.html')

from langdetect import detect
from django.http import JsonResponse
from django.shortcuts import render
import re
import openai
import re

import openai
import re

def is_latin(text):
    return bool(re.search(r"[a-zA-Z]", text))

def is_cyrillic(text):
    return bool(re.search(r"[а-яА-Я]", text))

def gramatik_tahrir(text):
    # Matn o‘zbek tilidami (lotin yoki kirill)?
    if not (is_latin(text) or is_cyrillic(text)):
        return text  # Tilda emas, o‘zgartirmay qaytariladi

    # Kirill yozuvi bo‘lsa, shunga mos ko‘rsatma beriladi
    if is_cyrillic(text):
        instruction = (
            "Quyidagi matndagi so‘zlarning grammatik va imloviy xatolarini kirill yozuvida to‘g‘irlang. "
            "Matndagi mavjud so‘zlar o‘zgartirilishi mumkin, lekin yangi so‘zlar qo‘shilmasin. "
            "Qisqartmalar to‘liq yozilsin. Matnning birinchi harfi katta bo‘lsin. Kirill yozuvida yozilgan holda qaytaring."
        )
    else:
        instruction = (
            "Quyidagi matndagi so‘zlarning grammatik va imloviy xatolarini to‘g‘irlang, masalan: 'maytab' so‘zi 'maktab' ga. "
            "Matndagi mavjud so‘zlar o‘zgartirilishi mumkin, lekin yangi so‘zlar qo‘shilmasin. "
            "Matnda qisqartirib yozilgan so‘zlar to‘g‘irlansin. Matnning birinchi harfi katta harf bilan boshlanishi kerak."
        )

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Siz grammatik va uslubiy tahrir qilishda yordam beruvchi yordamchisiz."},
            {"role": "user", "content": f"{instruction}\n\n{text}"}
        ],
        temperature=0.7,
    )

    tahrirlangan_matn = response['choices'][0]['message']['content'].strip()
    return tahrirlangan_matn



def tahrir(request):
    error = False
    if request.POST:
        text = request.POST['text']
        if len(text) > 10:
            if is_latin(text) or is_cyrillic(text):
                data = gramatik_tahrir(text)
                return JsonResponse({'response': data})
            else:
                print("Matn o‘zbek tilida emas yoki aralash yozuvda.")
                return JsonResponse({'error': "Faqat o‘zbek lotin yoki o‘zbek kirill yozuvidagi matnlar qabul qilinadi."})
        else:
            error = True
    return render(request, 'tahrir.html', {'error': error})
# def tahrir(request):
#
#     if request.POST:
#         data=gramatik_tahrir((request.POST['text']))
#         return JsonResponse({'response': data})
#     return render(request, 'tahrir.html')


class GrammarCorrectionView(APIView):
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']

            openai.api_key = API_KEY
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                # messages=[
                #     {"role": "system",
                #      "content": "Siz grammatik va uslubiy tahrir qilishda yordam beruvchi yordamchisiz."},
                #     {"role": "user",
                #      "content": f"Quyidagi matnni grammatik va uslubiy jihatdan to'g'rilab bering:\n\n{text}"}
                # ],
                messages=[
                    {"role": "system",
                     "content": "Siz grammatik va uslubiy tahrir qilishda yordam beruvchi yordamchisiz."},
                    {"role": "user",
                     "content": f"Quyidagi matndagi so‘zlarning grammatik va imloviy xatolarini to‘g‘irlang, masalan: 'maytab' so‘zi 'maktab' ga. Matndagi mavjud so‘zlar o‘zgartirilishi mumkin, lekin yangi so‘zlar qo‘shilmasin. Matnda qisqartirib yozilgan so‘zlar to‘g‘irlansin. Matnning birinchi harfi katta harf bilan boshlanishi kerak. \n\n{text}"}
                    # {"role": "user", "content": f"Quyidagi matndagi so'zlarning xatosini to'g'rilab bering, matnga qo'shimcha so'zlar qo'shilmasin, matndagi birinchi harf katta bo'lsin: \n\n{text}"} # bn, bilan
                    # {"role": "user", "content": f"Quyidagi matnni grammatik va uslubiy jihatdan to'g'rilab bering:\n\n{text}"} # optimal
                ],
                temperature=0.7,
            )

            tahrirlangan_matn = response['choices'][0]['message']['content'].strip()
            return Response({"corrected_text": tahrirlangan_matn}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)