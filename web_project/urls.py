from django.contrib import admin
from django.urls import include, path
from web_project import views


urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("", include(('product.urls', 'product'), namespace='product')),
    path("products/katanas/", views.katanas, name='katanas'),
    path("products/nodachis/", views.nodachis, name='nodachis'),
    path("user/createUser/", views.createUser, name='createUser'),
    path("user/login/", views.login, name='login'),
]