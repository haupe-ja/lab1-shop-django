from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    # Pobiera produkt o ID 1
    single_product = Product.objects.get(pk=1)

    # Po kategorii: Aby wyświetlić produkty z kategorii o ID 2
    filtered = Product.objects.filter(category=2)

    # Po producencie: Aby wyświetlić produkty od producenta o ID 3
    filtered = Product.objects.filter(manufacturer=3)
    
    return HttpResponse(single_product)