from django.contrib import admin

# Register your models here.

from compras.models import Producto, Pedido, Lineapedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['usuario','fecha']

class LineapedidoAdmin(admin.ModelAdmin):
    list_display = ['productop','pedidoid','cantidad']


admin.site.register(Producto)
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Lineapedido,LineapedidoAdmin)