from django.urls import include, path

from product import views

app_name = 'product'

urlpatterns = [
    path("productList/", views.productList, name="productList"),
    path("createProduct/", views.createProduct, name="createProduct"),
    path("showProduct/<int:id>/", views.showProduct, name="showProduct"),
    path("editProduct/<int:id>/", views.editProduct, name="editProduct"),
    path("removeProduct/", views.removeProduct, name="removeProduct"),
    path('product/<int:id>/<slug:productSlug>/', views.showSpecificProduct, name='showSpecificProduct'),
    
]