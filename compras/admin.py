from django.contrib import admin

# Register your models here.

from compras.models import Producto, Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['usuario','fecha','productop','cantidad']

admin.site.register(Producto)
admin.site.register(Pedido,PedidoAdmin)