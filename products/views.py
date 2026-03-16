from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

def index(request):
    # Wyciąganie wszystkich kategorii do menu bocznego
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'base.html', context)

def category_view(request, id):
    # Pobieranie konkretnej kategorii oraz produktów do niej przypisanych
    specific_category = Category.objects.get(pk=id)
    category_products = Product.objects.filter(category=specific_category)
    categories = Category.objects.all()
    
    context = {
        'specific_category': specific_category,
        'category_products': category_products,
        'categories': categories
    }
    return render(request, 'category_product.html', context)

def product_view(request, id):
    # Pobieranie jednego konkretnego produktu
    single_product = Product.objects.get(pk=id)
    categories = Category.objects.all()
    
    context = {
        'single_product': single_product,
        'categories': categories
    }
    return render(request, 'product.html', context)