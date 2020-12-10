from cart.cart import Cart

def sumCart(request):
    cart = Cart(request)

    qty = cart.getCartQty()
    cartPrice = cart.getCartPrice()
    
    return { 'qty': qty, 'cartPrice': cartPrice}