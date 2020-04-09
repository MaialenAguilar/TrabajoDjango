from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('clientes/<int:cliente_id>/', views.detalle, name='detalle'),
 ]