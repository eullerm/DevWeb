from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.template.loader import render_to_string

from product.models import Product
from createAjax.models import ProductAjax
from django.core.paginator import Paginator
from product.forms import FormSearchProduct, ProductForm
from createAjax.forms import ProductFormAjax, QuantityForm

from django.contrib import messages
from django.http import JsonResponse
from category.models import Category
from django.template.defaultfilters import slugify
from django.core import serializers


def createProductAjax(request):
    # request should be ajax and method should be POST.
    print(request.is_ajax)


    products = ProductAjax.objects.all()
    valorEmEstoque = 0
    listaDeItens=[]
    for product in products:
        valorEmEstoque += float(product.price) * float(product.quantity)
        listaDeItens.append({'id':product.id,
                            'name':product.name, 
                            'price':product.price, 
                            'quantity':QuantityForm(initial={'quantity':product.quantity, 'productId': product.id}), 
                            'category':product.category, 
                            'total': product.quantity*product.price}
                            )
    valorEmEstoque = round(valorEmEstoque, 2)
    if request.method == "POST":
        # get the form data
        form = ProductFormAjax(request.POST)
        print(form.is_valid())
        # save the data and after fetch the object in instance
        if form.is_valid():
            product = form.save(commit = False)
            product.slug = slugify(product.name)
            product.save()
            item = {'id':product.id,'name':product.name, 'price':product.price, 'quantity':QuantityForm(initial={'quantity':product.quantity,  'productId': product.id}), 'category':product.category, 'total': product.quantity*product.price}
            template = loader.get_template('createAjax/tableRow.html')
            rowTabela = template.render({'product': item}, request)
            print("oi")
            valorEmEstoque = 0
            products = ProductAjax.objects.all()
            for product in products:
                valorEmEstoque += float(product.price) * float(product.quantity)
            return JsonResponse({'row':rowTabela, 'formValido':True,'total':valorEmEstoque}, status = 200)
        else:
            print("else1")
            return render(request, 'createAjax/formCreateProductAjax.html', {'form': form})


    # if method is GET
    else:
        print("else2")
        form = ProductFormAjax()
    return render(request, 'createAjax/createProductAjax.html',{'form': ProductFormAjax, 'products':listaDeItens, 'total':valorEmEstoque})


def updateProductAjax(request):
    if request.POST:
        quantidadeForm = QuantityForm(request.POST)
        if(quantidadeForm.is_valid()):
            id = quantidadeForm.cleaned_data['productId']
            qtd = quantidadeForm.cleaned_data['quantity']
            product = get_object_or_404(ProductAjax, id=id)
            product.quantity = qtd
            product.save()
            produtos = ProductAjax.objects.all()
            total = 0
            for p in produtos:
                total += float(p.quantity)*float(p.price)
            total = round(total, 2)
            print(total)
            item = {'id':product.id,
                    'name':product.name, 
                    'price':product.price, 
                    'quantity':QuantityForm(initial={'quantity':product.quantity,  'productId': product.id}), 
                    'category':product.category, 
                    'total': product.quantity*product.price}

            template = loader.get_template('productAjax/tableRow.html')
            rowTabela = template.render({'product': item}, request)
            print(rowTabela)
            return JsonResponse({'row': rowTabela, 'total':total}, status=200)
    return redirect('createAjax:createProductAjax')

def removeProductAjax(request, id):
    produto = get_object_or_404(ProductAjax, pk=id)
    produto.delete()
    produtos = ProductAjax.objects.all()
    total = 0
    for p in produtos:
        total += float(p.quantity)*float(p.price)
    total = round(total, 2)
    print("oi")
    return JsonResponse({'total':round(total, 2), 'row':'' }, status=200)

