from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Division, District, Category


# Create your views here.
def product_list(request):
    return render(request, "model_main/base.html", )


def api_data(request):
    data = {
        'division': list(Division.objects.values()),
        'category': list(Category.objects.values()),

    }
    return JsonResponse(data, safe=False)


def api_district(request):
    queryAll = District.objects
    if request.GET.get('division'):
        queryAll = queryAll.filter(division=request.GET.get('division'))

    district = queryAll.values()
    data = {
        'district': list(district),

    }
    return JsonResponse(data, safe=False)
