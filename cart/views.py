from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sessions.models import Session


def cart_details(request, tot=0, count=0, cart_items=None):
    ct_items = []  # Initialize ct_items with an empty list
    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
        ct_items = item.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.prodt.price * i.quan)
            count += i.quan
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count})
    # return HttpResponse('you are in cart')


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        request.session.create()
        ct_id = request.session.session_key
    return ct_id


# Make sure you use the correct model name here

def add_cart(request, product_id):
    print("cart")
    prod = Products.objects.get(id=product_id)  # Correct the model name
    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))  # Correct the model name
    except Cartlist.DoesNotExist:
        ct = Cartlist.objects.create(cart_id=c_id(request))  # Correct the model name
        ct.save()
    try:
        c_items = item.objects.get(prodt=prod, cart=ct)  # Correct the model name
        if c_items.quan < c_items.prodt.stock:
            c_items.quan += 1  # Increment the quantity
            c_items.save()
    except item.DoesNotExist:
        c_items = item.objects.create(prodt=prod, quan=1, cart=ct)  # Correct the model name
        c_items.save()
    return redirect('cart_details')  # Correct the URL name


def min_cart(request, product_id, prod=None):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(prodt=prod, cart=ct)
    c_items = item.objects.get(prodt=prod, cart=ct)
    if c_items.quan > 1:
        c_items.quan -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')


def cart_delete(request, product_id, prod=None):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(prodt=prod, cart=ct)
    c_items = item.objects.get(prodt=prod, cart=ct)
    return redirect('cartDetails')
