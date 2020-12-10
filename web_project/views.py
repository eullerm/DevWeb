from django.shortcuts import render, get_object_or_404
from product.models import Product
from category.models import Category
from cart.cart import Cart
from cart.forms import QtyForm


def index(request):
    bestSeller = Product.objects.filter(bestSeller=True).order_by('name')

    cart = Cart(request)

    formList = []

    for product in bestSeller:
        qty = cart.getTotalQty(product.id)
        formList.append(QtyForm(initial={'qty': qty, 'product_id': product.id}))

    return render(request, 'index.html', {'list': zip(bestSeller, formList)})


def katanas(request):
    category = get_object_or_404(Category, slug='katana')
    print(category)
    katanasList = Product.objects.filter(category=category).order_by('name')
    print(katanasList)

    cart = Cart(request)

    formList = []

    for product in katanasList:
        qty = cart.getTotalQty(product.id)
        formList.append(QtyForm(initial={'qty': qty, 'product_id': product.id}))

    return render(request, 'products/productsPages.html', {"list": zip(katanasList, formList), 'category': category})

def nodachis(request):
    category = get_object_or_404(Category, name='Nodachi')
    print(category)
    nodachisList = Product.objects.filter(category=category).order_by('name')
    print(nodachisList)

    cart = Cart(request)

    formList = []

    for product in nodachisList:
        qty = cart.getTotalQty(product.id)
        formList.append(QtyForm(initial={'qty': qty, 'product_id': product.id}))

    return render(request, 'products/productsPages.html', {"list": zip(nodachisList,formList), 'category': category})

def all(request):
    all = Product.objects.order_by('name')
    print(all)
    return render(request, 'products/productsPages.html', {"products": all})

def createUser(request):
    return render(request, 'user/create/createUser.html')

def login(request):
    return render(request, 'user/login/signIn.html')

def about(request):
    return render(request, 'business/about.html')

def checkout(request):
    return render(request, 'payment/checkout.html')