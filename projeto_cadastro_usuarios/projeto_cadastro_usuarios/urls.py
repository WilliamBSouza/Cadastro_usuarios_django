from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    #rota, view responsável, nome de referência
    #facebook.com  Exemplo
    path("",views.home, nome = "home"),
    #facebook.com/William Exemplo
    #path("William/")  Exemplo

]
