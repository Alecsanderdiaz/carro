from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',

    url(r'^$', 'compras.views.home', name='home'),
    url(r'^pagina2/$', 'compras.views.pagina2', name='pagina2'),
    url(r'^pagina3/$', 'compras.views.pagina3', name='pagina3'),
    url(r'^carro/$', 'compras.views.carro', name='carro'),
    url(r'^alcarrito/(?P<p_id>\d+)/$', 'compras.views.alcarrito', name='alcarrito'),
    url(r'^vaciarcarro/$', 'compras.views.vaciarcarro', name='vaciarcarro'),
    url(r'^labs/mimeteo$', TemplateView.as_view(template_name="mimeteo.html")),
    url(r'^mandarpedido/$','compras.views.mandarpedido', name='mandarpedido'),
    url(r'^ingresar/$','compras.views.ingresar', name='ingresar'),
    url(r'^cerrar/$','compras.views.cerrar', name='cerrar'),



)