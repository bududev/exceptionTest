# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from main.models import Main
from main.serializers import MainSerializer

@csrf_exempt
def main_list(request):
    """
    List all code mains, or create a new main.
    """

    if request.method == 'GET':
        mains = Main.objects.all()
        serializer = MainSerializer(mains, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MainSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def main_exception(request):
    """
    Occur exception
    """

    i = 1 / 0