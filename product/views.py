from django.shortcuts import get_object_or_404, redirect, render
from product.models import Product
from django.core.paginator import Paginator
from product.forms import FormSearchProduct, ProductForm
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# @login_required(login_url='/authentication/login')
# @staff_member_required('login_ur='authentication/login')
# @user_passes_test(lambda u: u.is_superuser)
@user_passes_test(lambda u: u.is_staff)
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


@user_passes_test(lambda u: u.is_staff)
def bestSeller(request):
    productList = Product.objects.filter(bestSeller__icontaines=True).order_by('name')
    return productList


@user_passes_test(lambda u: u.is_staff)
def createProduct(request):

    if request.POST:
        product_id = request.session.get('product_id')

        if product_id:
            product = get_object_or_404(Product, pk = product_id)
            productForm = ProductForm(request.POST, request.FILES, instance = product)

        else:
            productForm = ProductForm(request.POST, request.FILES)

        if productForm.is_valid():
            product = productForm.save(commit = False)
            product.slug = slugify(product.name)
            product.save()

            if product_id:
                messages.add_message(request, messages.INFO, "Produto alterado com sucesso!")
                del request.session['product_id']

            else:
                messages.add_message(request, messages.INFO, "Produto cadastrado com sucesso!")

            return redirect('product:showProduct', id = product.id)

    else:
        try:
            del request.session['product_id']
        except KeyError:
            pass
        productForm = ProductForm()

    return render(request, 'product/createProduct.html',{'form': productForm})


@user_passes_test(lambda u: u.is_staff)
def showProduct(request, id):
    product = get_object_or_404(Product, pk=id)
    request.session['product_id_del'] = id
    return render(request, 'product/showProduct.html', {'product': product})

@user_passes_test(lambda u: u.is_staff)
def editProduct(request, id):
    product = get_object_or_404(Product, pk=id)

    product_form = ProductForm(instance = product)

    request.session['product_id'] = id
    
    return render(request, 'product/createProduct.html', {'form': product_form})

@user_passes_test(lambda u: u.is_staff)
def removeProduct(request):
    product_id = request.session.get('product_id_del')
    product = get_object_or_404(Product, pk=product_id)
    product.image.delete()
    product.delete()

    del request.session['product_id_del']
    messages.add_message(request, messages.INFO, 'Produto removido com sucesso.')

    return render(request, 'product/showProduct.html', {'product': product})

def showSpecificProduct(request, id, productSlug):
    product = get_object_or_404(Product, pk=id)
    request.session['product_id_del'] = id
    return render(request, 'products/specificProduct/specificProduct.html', {'product': product})