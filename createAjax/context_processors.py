from createAjax.models import ProductAjax

def ProductAjax(request):
    product = ProductAjax(request)

    qty = product.getQty()
    price = product.getPrice()
    name = product.getName()
    category = product.getCategory()
    
    return { 'qty': qty,  
            'price': price, 
            'name': name, 
            'category': category}