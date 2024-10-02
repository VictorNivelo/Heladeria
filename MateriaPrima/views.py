from django.http import HttpResponse
from django.template import loader

from MateriaPrima.models import MateriaPrima


def MateriaPrimahttp(request):
    template = loader.get_template('Heladeria/MateriaPrima.html')
    materiaPrimas = MateriaPrima.objects.all()
    context = {
        'materiaPrimas': materiaPrimas,
    }
    return HttpResponse(template.render(context, request))

def MateriaPrima_Detalle(request, MateriaPrima_id):
    materiaPrima = MateriaPrima.objects.first()
    return HttpResponse('hola helados xd: %s '% materiaPrima.nombre_producto)