from django.urls import include, path

from category import views

app_name = 'category'

urlpatterns = [
    path("categoryList/", views.categoryList, name="categoryList"),
    path("createCategory/", views.createCategory, name="createCategory"),
    path("showCategory/<int:id>/", views.showCategory, name="showCategory"),
    path("editCategory/<int:id>/", views.editCategory, name="editCategory"),
    path("removeCategory/", views.removeCategory, name="removeCategory"),
    
]