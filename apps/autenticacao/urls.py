from django.urls import path
from apps.autenticacao.views import logar, deslogar

urlpatterns = [
    path('logar/', logar, name='logar'),
    path('deslogar/', deslogar, name='deslogar'),
]
