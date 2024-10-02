from django.http import HttpResponse
from django.template import loader

from Facturas.models import Factura, DatosUsuario
from Heladeria.models import Helado, Cono, Galleta, Pastel
from MateriaPrima.models import MateriaPrima


def Heladeria(request):
    template = loader.get_template('Heladeria/Heladeria.html')
    heladeria = "Mamahuevo"
    context = {
        'heladeria': heladeria,
    }
    return HttpResponse(template.render(context, request))

def Heladohttp(request):
    template = loader.get_template('Heladeria/Helados.html')
    helados = Helado.objects.all()
    context = {
        'helados': helados,
    }
    return HttpResponse(template.render(context, request))

def Helado_Detalle(request, Helado_id):
    helado = Helado.objects.first()
    return HttpResponse('hola helados xd: %s '% helado.sabor_Helado)

def Conohttp(request):
    template = loader.get_template('Heladeria/Cono.html')
    Conos = Cono.objects.all()
    context = {
        'Conos': Conos,
    }
    return HttpResponse(template.render(context, request))

def Cono_Detalle(request, Cono_id):
    cono = Cono.objects.first()
    return HttpResponse('hola cono xd: %s '% cono.sabor_Cono)

def Galletahttp(request):
    template = loader.get_template('Heladeria/Galleta.html')
    Galletas = Galleta.objects.all()
    context = {
        'Galletas': Galletas,
    }
    return HttpResponse(template.render(context, request))

def Galleta_Detalle(request, Galleta_id):
    galleta = Galleta.objects.first()
    return HttpResponse('hola Galleta xd: %s '% galleta.sabor_Galleta)

def Pastelhttp(request):
    template = loader.get_template('Heladeria/Pastel.html')
    Pasteles = Pastel.objects.all()
    context = {
        'Pasteles': Pasteles,
    }
    return HttpResponse(template.render(context, request))

def Pastel_Detalle(request, Pastel_id):
    pastel = Pastel.objects.first()
    return HttpResponse('hola Pastel xd: %s '% pastel.sabor_Pastel)

def EmpresaHeladoshttp(request):
    return HttpResponse('Empresa Helados')

def Facturahttp(request):
    template = loader.get_template('Heladeria/Factura.html')
    facturas = Factura.objects.all()
    context = {
        'facturas': facturas,
    }
    return HttpResponse(template.render(context, request))

def Factura_Detalle(request, Factura_id):
    factura = Factura.objects.first()
    return HttpResponse('hola helados xd: %s '% factura.NombreLocal)

def DatosUsuariohttp(request):
    template = loader.get_template('Heladeria/DatosUsuario.html')
    datosUsuario = DatosUsuario.objects.all()
    context = {
        'datosUsuario': datosUsuario,
    }
    return HttpResponse(template.render(context, request))

def DatosUsuario_Detalle(request, DatosUsuario_id):
    datosUsuario = DatosUsuario.objects.first()
    return HttpResponse('hola helados xd: %s '% DatosUsuario.nombre_usuario)

def ImprimirFacturahttp(request):
    template = loader.get_template('Heladeria/ImprimirFactura.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def ImprimirFactura_Detalle(request, ImprimirFactura_id):
    return HttpResponse('')

def MateriaPrimahttp(request):
    template = loader.get_template('Heladeria/MateriaPrima.html')
    materiaPrimas = MateriaPrima.objects.all()
    context = {
        'materiaPrimas': materiaPrimas,
    }
    return HttpResponse(template.render(context, request))

def MateriaPrima_Detalle(request, MateriaPrima_id):
    materiaPrima = MateriaPrima.objects.first()
    return HttpResponse('hola helados xd: %s '% materiaPrima.nombre_usuario)

def FacturacionMateriaPrimahttp(request):
    template = loader.get_template('Heladeria/FacturacionMateria.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def FacturacionMateriaPrima_Detalle(request, FacturacionMateriaPrima_id):
    return HttpResponse('')

def Formulariohttp(request):
    template = loader.get_template('Heladeria/Formulario.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def Formulario_Detalle(request, Formulario_id):
    return HttpResponse('')

def ElegirUsuariohttp(request):
    template = loader.get_template('Heladeria/ElegirUsuario.html')
    datosUsuario = DatosUsuario.objects.all()
    context = {
        'datosUsuario': datosUsuario,
    }
    return HttpResponse(template.render(context, request))

def ElegirUsuario_Detalle(request, ElegirUsuario_id):
    datosUsuario = DatosUsuario.objects.first()
    return HttpResponse('hola helados xd: %s '% DatosUsuario.nombre_usuario)