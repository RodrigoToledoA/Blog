from django.template import RequestContext
from django.shortcuts import render_to_response, render, redirect
from blog.models import Entrada, Contacto, Mensajes
from django.core.mail import send_mail
from django.conf import settings

import os

# Create your views here.
def home(request):
    context = RequestContext(request)
    posts = Entrada.objects.filter(published = True)
    return render_to_response('home.html', 
                              {'posts':posts},
                              context)

def ver_post(request,id_post):
    context = RequestContext(request)
    mi_post = Entrada.objects.get(id = id_post)
    mensajes = Mensajes.objects.filter(published_in = mi_post, published = True)

    return render_to_response('post.html',
                              {'post':mi_post,
                               'mensajes':mensajes},
                              context)

def contact(request):
    context = RequestContext(request)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        celu = request.POST['celu']
        mail= request.POST['mail']
        mensaje= request.POST['mensaje']
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.celu = celu
        contacto.mail = mail
        contacto.mensaje = mensaje
        contacto.save()
        send_mail('Bienvenido a la comunidad', 'Te has registrado correctamente en el blog.\n Porque has decidido contactarnos?', 'rodry.toledo@gmail.com', [mail], fail_silently=False)


        return render_to_response('contact.html', 
                                  {'enviado':enviado},
                                  context)

def save_message(request):
    context = RequestContext(request)
    mensajes = None
    if request.method == 'POST':
        mi_post = Entrada.objects.get(id=request.POST['id'])
        nombre= request.POST['nombre']
        mensaje= request.POST['mensaje']        
        msje = Mensajes()
        msje.nombre = nombre
        msje.mensaje = mensaje
        msje.published_in = mi_post
        msje.save()
        mensajes = Mensajes.objects.filter(published_in=mi_post, published = True)

        return render_to_response('mensajes.html', 
                                  {'mensajes':mensajes},
                                  context)

def calculadora(request):
    context = RequestContext(request)
    return render_to_response('calculadora.html',
                              context)
def curriculum(request):
    context = RequestContext(request)
    return render_to_response('Curriculum.html',
                              context)

def cambio_moneda(request):
    context = RequestContext(request)
    return render_to_response('cambio.html',
                              context)

def cronometro(request):
    context = RequestContext(request)
    return render_to_response('cronometro.html',
                              context)

def galeria(request):
    context = RequestContext(request)
    return render_to_response('imagenes.html',
                              context)

def contacto(request):
    context = RequestContext(request)
    if request.method == 'POST':
        nombre = request.POST['nombre']
        celu = request.POST['celu']
        mail= request.POST['mail']
        mensaje= request.POST['mensaje']
        
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.celu = celu
        contacto.mail = mail
        contacto.mensaje = mensaje
        contacto.save()
        
        from_user = settings.EMAIL_HOST_USER
        send_mail("Bienvenido a la comunidad", "Te has registrado correctamente en el blog. Porque has decidido contactarnos?", from_user, [mail], fail_silently=False)

    return render_to_response('Contacto.html',
                              context)

def formulario(request):
    context = RequestContext(request)
    return render_to_response('formulario.html',
                              context)