from django.shortcuts import get_object_or_404, render
from category.models import Category
from cart.models import CartTable
from cart.cart import Cart
from cart.forms import QtyForm
from django.http.response import HttpResponse
from product.models import Product
from django.core.signing import Signer


def listProduct(request, categorySlug = None):

    category = None
    
    products = Product.objects.filter(available = True).order_by('name')

    if categorySlug:
        category = get_object_or_404(Category, slug = categorySlug)
        products = Product.objects.filter(available = True, category = category).order_by('name')

    cart = Cart(request)

    formList = []

    for product in products:
        qty = cart.getTotalQty(product.id)
        formList.append(QtyForm(initial={'qty': qty, 'product_id': product.id}))

    return render(request, 'cart/shoppingCart.html', {'list': zip(products, formList), 'category': category})

def showProduct(request, id, productSlug):

    #product = get_object_or_404(Product, id=id)

    pass
    
    #return render(request, 'products/specificProduct/specificProducts.html', {'product': product})

def attCart(request):
    form = QtyForm(request.POST)

    if form.is_valid():
        product_id = form.cleaned_data['product_id']
        qty = form.cleaned_data['qty'] 

        cart = Cart(request)

        if qty == 0:
            cart.remove(product_id)
            totalPrice = 0.0

        else:
            cart.att(product_id, qty)
            totalPrice = cart.getTotalPrice(product_id)

#        qtyTotal = cart.getCartQty()

#        cartPrice = cart.getCartPrice

#        print('***** id do produto = ' + product_id +
#              '  quantidade = ' + str(qty) +
#              '  preço total do produto = ' + str(totalPrice))
#        print('***** qtd no carrinho = ' + str(qtyTotal) +
#              '  valor do carrinho = ' + str(cartPrice))

        return render(request, 'answerAjax.html', {'totalPrice': totalPrice,})

    else:
        raise ValueError("Ocorreu um erro inesperado ao adicionar um produto no carrinho.")


def showCart(request):

    cart = Cart(request)

    productsCart = cart.getProduct()

    cartPrice = cart.getCartPrice()

    formList = []

    for product in productsCart:
        print(product)
        qty = cart.getTotalQty(product['id'])
        formList.append(QtyForm(initial={'qty': qty, 'product_id': product['id']}))

    return render(request, 'cart/shoppingCart.html', {'products': zip(productsCart, formList), 'cartPrice': cartPrice})


def checkOut(request):
    cart = Cart(request)

    productsCart = cart.getProduct()

    cartPrice = cart.getCartPrice()

    formList = []

    for product in productsCart:
        print(product)
        qty = cart.getTotalQty(product['id'])
        formList.append(QtyForm(initial={'qty': qty, 'product_id': product['id']}))

    return render(request, 'payment/checkout.html', {'products': zip(productsCart, formList), 'cartPrice': cartPrice})