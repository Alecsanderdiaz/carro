from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'compras.views.home', name='home'),
    url(r'^pagina2/$', 'compras.views.pagina2', name='pagina2'),
    url(r'^pagina3/$', 'compras.views.pagina3', name='pagina3'),
    url(r'^carro/$', 'compras.views.carro', name='carro'),

    url(r'^vaciarcarro/$', 'compras.views.vaciarcarro', name='vaciarcarro'),

    url(r'^mandarpedido/$','compras.views.mandarpedido', name='mandarpedido'),
    url(r'^ingresar/$','compras.views.ingresar', name='ingresar'),
    url(r'^cerrar/$','compras.views.cerrar', name='cerrar'),
    url(r'^buscar/$','compras.views.buscar', name='buscar'),



)