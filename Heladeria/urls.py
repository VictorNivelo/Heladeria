from django.urls import path
from Heladeria import views

urlpatterns =[
    path('', views.Heladeria, name='index'),

    path('Helado', views.Heladohttp, name='Helado'),
    path('Helado/<int:Helado_id>', views.Helado_Detalle, name='Helado'),

    path('Cono', views.Conohttp, name='Cono'),
    path('Cono/<int:Cono_id>', views.Cono_Detalle, name='Cono'),

    path('Galleta', views.Galletahttp, name='Galleta'),
    path('Galleta/<int:Galleta_id>', views.Galleta_Detalle, name='Galleta'),

    path('Pastel', views.Pastelhttp, name='Pastel'),
    path('Pastel/<int:Pastel_id>', views.Pastel_Detalle, name='Pastel'),

    path('EmpresaHelados', views.EmpresaHeladoshttp, name='EmpresaHelados'),

    path('Factura', views.Facturahttp, name='Factura'),
    path('Factura/<int:Factura_id>', views.Factura_Detalle, name='Factura'),

    path('DatosUsuario', views.DatosUsuariohttp, name='DatosUsuario'),
    path('DatosUsuario/<int:DatosUsuario_id>', views.DatosUsuario_Detalle, name='DatosUsuario'),

    path('ImprimirFactura', views.ImprimirFacturahttp, name='ImprimirFactura'),
    path('ImprimirFactura/<int:ImprimirFactura_id>', views.ImprimirFactura_Detalle, name='ImprimirFactura'),

    path('MateriaPrima', views.MateriaPrimahttp, name='MateriaPrima'),
    path('MateriaPrima/<int:MateriaPrima_id>', views.MateriaPrima_Detalle, name='MateriaPrima'),

    path('FacturacionMateriaPrima', views.FacturacionMateriaPrimahttp, name='FacturacionMateriaPrima'),
    path('FacturacionMateriaPrima/<int:FacturacionMateriaPrima_id>', views.FacturacionMateriaPrima_Detalle, name='FacturacionMateriaPrima'),

    path('Formulario', views.Formulariohttp, name='Formulario'),
    path('Formulario/<int:Formulario_id>', views.Formulario_Detalle,name='Formulario'),

    path('ElegirUsuario', views.ElegirUsuariohttp, name='ElegirUsuario'),
    path('ElegirUsuario/<int:ElegirUsuario_id>', views.ElegirUsuario_Detalle,name='ElegirUsuario'),

]