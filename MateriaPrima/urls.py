from django.urls import path
from MateriaPrima import views

urlpatterns =[
    path('MateriaPrima', views.MateriaPrimahttp, name='MateriaPrima'),
    path('MateriaPrima/<int:MateriaPrima_id>', views.MateriaPrima_Detalle, name='MateriaPrima'),
    ]