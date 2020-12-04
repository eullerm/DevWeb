from django.contrib.auth import views as auth_views
from importlib.resources import path

app_name = 'authentication'

urlpatterns = [
    #path('authentication/login/', auth_views.LoginView.as_view(template_name='user/login/signIn.html'), name='login'),
    #path('authentication/logout/', auth_views.LogoutView.as_view(), name='logout'),
]