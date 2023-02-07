from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', views.main, name="index"),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/<str:slug_categoria>/',
         views.listar_produtos, name='listar_produtos_por_categoria'),
    path('produto/<str:id>/<str:slug_produto>/',
         views.detalhes_produto, name='detalhes_produto'),
]
