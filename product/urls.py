from django.urls import include, path

from product import views

app_name = 'product'

urlpatterns = [
    path("productList/", views.productList, name="productList"),
    
]