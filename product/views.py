from django.shortcuts import render
from product.models import Product
from django.core.paginator import Paginator
from product.forms import FormSearchProduct

def productList(request):
    
    form = FormSearchProduct(request.GET)

    if(form.is_valid()):
        name = form.cleaned_data['name']
        productList = Product.objects.filter(name__icontains=name).order_by('name')
        paginator = Paginator(productList, 3)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        print(productList)
        print(page_obj)


        return render(request, 'product/productSearch.html', {'products': page_obj, 'form': form, 'name': name})
    
    else:
        raise ValueError("Ocorreu um erro inesperado ao tentar recuperar um produto.")

def bestSeller(request):
    productList = Product.objects.filter(bestSeller__icontaines=True).order_by('name')
    return productList