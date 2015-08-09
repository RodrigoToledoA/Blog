from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'blog.views.home', name='home'),
                       url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'blog.views.ver_post', name='vermipost'),
                       url(r'^contactame/$', 'blog.views.contact', name='contactame'),
                       url(r'^save_message/$', 'blog.views.save_message', name='save_message'), 
                       url(r'^calculator/$', 'blog.views.calculadora', name='calculadora'),                     
                       url(r'^cambio/$', 'blog.views.cambio_moneda', name='cambio'),
                       url(r'^cronometro/$', 'blog.views.cronometro', name='cronometro'),  
                       url(r'^galeria/$', 'blog.views.galeria', name='galeria'), 
                       url(r'^formulario/$', 'blog.views.formulario', name='formulario'),
                       url(r'^curriculum/$', 'blog.views.curriculum', name='curriculum'), 
                       url(r'^contacto/$', 'blog.views.contacto', name='contacto')
                      )