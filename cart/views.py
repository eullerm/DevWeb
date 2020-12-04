from django.shortcuts import get_object_or_404, render
from category.models import Category
from product.models import Product


def listProduct(request, categorySlug = None):

    category = None

    categories = Category.objects.all().order_by('name')

    products = Product.objects.filter(available = True).order_by('name')

    if categorySlug:
        category = get_object_or_404(Category, slug=categorySlug)
        products = Product.objects.filter(category = category).order_by('name')

    pass
    #return render(request, 'cart/listProduct.html', {'categories': categories, 'products': products, 'category': category})


def showProduct(request, id, productSlug):

    product = get_object_or_404(Product, id=id)

    pass
    
    #return render(request, 'products/specificProduct/specificProducts.html', {'product': product})

