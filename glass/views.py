from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.template.context import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect

def home(request):
    hola="here"
    nombrep="Esta es otra prueba"
    compania = "Master auto Glass"
    c = {'hola':hola,'nombre':nombrep,'compa':compania,}
    return render_to_response('home.html',c)

def servicios(request):
    titulo = "SERVICIOS"
    c = {'titulo':titulo}
    return render_to_response('servicios.html',c)


def detalleservice(request):
    titulo = "Detalle de los servicios"
    c = {'titulo': titulo}
    return render_to_response('detalleservices.html',c)
