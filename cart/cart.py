from web_project import settings
from product.models import Product
from decimal import Decimal


class Cart(object):

    def __init__(self, request):
        self.session = request.session

        self.cart = self.session.get(settings.CART_SESSION_ID)

        if not self.cart:
            self.cart = self.session[settings.CART_SESSION_ID] = {}

    def att(self, id, qty):

        product = Product.objects.get(id=id, available = True)

        if id not in self.cart:
            self.cart[id] = {'id': id, 'price': str(product.price), 'qty': qty, 
                                'totalPrice': str(product.price * qty)}

        else:
            self.cart[id]['qty'] = qty
            self.cart[id]['totalPrice'] = str(self.cart[id]['qty'] * Decimal(self.cart[id]['price']))

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def getTotalPrice(self, id):
        return self.cart[id]['totalPrice']

    def getTotalQty(self, id):

        id = str(id)

        if id in self.cart:
            return self.cart[id]['qty']
        else:
            return 0

    def getCartPrice(self):
        return sum(Decimal(item['totalPrice']) for item in self.cart.values())

    def getCartQty(self):
        return sum(item['qty'] for item in self.cart.values())

    def getProduct(self):

        productList = []

        for item in self.cart.values():

            product = Product.objects.get(id=item['id'])

            productList.append(
                {'product': product, 
                'id': item['id'], 
                'price': Decimal(item['price']), 
                'qty': item['qty'], 
                'totalPrice': Decimal(item['totalPrice'])
                })

        return productList
