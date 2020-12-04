from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from category.forms import FormSearchCategory, CategoryForm
from django.template.defaultfilters import slugify
from django.contrib import messages
from category.models import Category

def categoryList(request):
    
    form = FormSearchCategory(request.GET)

    if(form.is_valid()):
        name = form.cleaned_data['name']
        categoryList = Category.objects.filter(name__icontains=name).order_by('name')
        paginator = Paginator(categoryList, 3)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        print(categoryList)
        print(page_obj)


        return render(request, 'category/categorySearch.html', {'categorys': page_obj, 'form': form, 'name': name})
    
    else:
        raise ValueError("Ocorreu um erro inesperado ao tentar recuperar um produto.")

def createCategory(request):

    if request.POST:
        category_id = request.session.get('category_id')

        if category_id:
            category = get_object_or_404(Category, pk = category_id)
            categoryForm = CategoryForm(request.POST, request.FILES, instance = category)

        else:
            categoryForm = CategoryForm(request.POST, request.FILES)

        if categoryForm.is_valid():
            category = categoryForm.save(commit = False)
            category.slug = slugify(category.name)
            category.save()

            if category_id:
                messages.add_message(request, messages.INFO, "Categoria alterada com sucesso!")
                del request.session['category_id']

            else:
                messages.add_message(request, messages.INFO, "Categoria cadastrada com sucesso!")

            return redirect('category:showCategory', id = category.id)

    else:
        try:
            del request.session['category_id']
        except KeyError:
            pass
        categoryForm = CategoryForm()

    return render(request, 'category/createCategory.html',{'form': categoryForm})


def showCategory(request, id):
    category = get_object_or_404(Category, pk=id)
    request.session['category_id_del'] = id
    return render(request, 'category/showCategory.html', {'category': category})

def editCategory(request, id):
    category = get_object_or_404(Category, pk=id)

    category_form = CategoryForm(instance = category)

    request.session['category_id'] = id
    
    return render(request, 'category/createCategory.html', {'form': category_form})

def removeCategory(request):
    category_id = request.session.get('category_id_del')
    category = get_object_or_404(Category, pk=category_id)
    category.delete()

    del request.session['category_id_del']
    messages.add_message(request, messages.INFO, 'Categoria removida com sucesso.')

    return render(request, 'category/showCategory.html', {'categorys': category})
