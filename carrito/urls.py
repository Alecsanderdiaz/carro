from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carrito.views.home', name='home'),
    url(r'^inicio/', include('compras.urls')),
    #url(r'^producto/', include('website.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
