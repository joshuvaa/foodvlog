from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import *


# Create your views here.

def home(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = Products.objects.filter(category=c_page, available=True)
    else:
        prodt = Products.objects.all().filter(available=True)

    paginator = Paginator(prodt, 9)  # 9 products per page
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    cat = categ.objects.all()

    return render(request, 'index.html', {'pr': page, 'ct': cat, 'products': page})


def prodDetails(request, c_slug, product_slug):
    try:
        prod = Products.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'item.html', {'pr': prod})


def searching(request):
    prod = None
    query = None
    page = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))

        paginator = Paginator(prod, 9)  # 9 products per page
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

    return render(request, 'search.html', {'qr': query, 'pr': page})
