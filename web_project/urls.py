from django.contrib import admin
from django.urls import include, path
from web_project import settings, views
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("", include(('product.urls', 'product'), namespace='product')),
    path("", include(('category.urls', 'category'), namespace='category')),
    path("products/katanas/", views.katanas, name='katanas'),
    path("products/nodachis/", views.nodachis, name='nodachis'),
    path("user/createUser/", views.createUser, name='createUser'),
    path("user/login/", views.login, name='login'),
    path("payment/checkout/", views.checkout, name='checkout'),
    path("business/about/", views.about, name='about'),
    path("", include(('cart.urls', 'cart'), namespace='cart')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)