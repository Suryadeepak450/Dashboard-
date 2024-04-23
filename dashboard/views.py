
from django.shortcuts import render
from django.http import JsonResponse
from .models import Data

def get_data(request):
    data = Data.objects.all().values()
    return JsonResponse(list(data), safe=False)
