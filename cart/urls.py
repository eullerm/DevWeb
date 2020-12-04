from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.listProduct, name='listProduct'),
    path('cart/<slug:categorySlug>/', views.listProduct, name='listProductPerCategory'),
    path('product/<int:id>/<slug:productSlug>/', views.showProduct, name='showProduct'),
]