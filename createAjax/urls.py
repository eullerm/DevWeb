from django.urls import include, path

from createAjax import views

app_name = 'createAjax'

urlpatterns = [
    path("updateProductAjax/", views.updateProductAjax, name='updateProductAjax'),
    path("createProductAjax/", views.createProductAjax, name="createProductAjax"),
    path("removeProductAjax/<int:id>/", views.removeProductAjax, name='removeProductAjax')
]