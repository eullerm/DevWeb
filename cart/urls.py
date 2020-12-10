from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.showCart, name='showCart'),
    path('attCart/', views.attCart, name='attCart'),
    path('cart/checkout/', views.checkOut, name='checkOut'),
    path('cart/<slug:categorySlug>/', views.listProduct, name='listProductPerCategory'),
    path('product/<int:id>/<slug:productSlug>/', views.showProduct, name='showProduct'),
]