from django.shortcuts import render, get_object_or_404
from product.models import Product
from category.models import Category

def index(request):
    bestSeller = Product.objects.filter(bestSeller=True).order_by('name')
    print(bestSeller)
    return render(request, 'index.html', {"bestSeller": bestSeller})


def katanas(request):
    category = get_object_or_404(Category, slug='katana')
    print(category)
    katanasList = Product.objects.filter(category=category).order_by('name')
    print(katanasList)
    return render(request, 'products/productsPages.html', {"products": katanasList, 'category': category})

def nodachis(request):
    category = get_object_or_404(Category, name='Nodachi')
    print(category)
    nodachisList = Product.objects.filter(category=category).order_by('name')
    print(nodachisList)
    return render(request, 'products/productsPages.html', {"products": nodachisList, 'category': category})

def createUser(request):
    return render(request, 'user/create/createUser.html')

def login(request):
    return render(request, 'user/login/signIn.html')