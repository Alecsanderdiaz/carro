from django.contrib import admin

# Register your models here.

from compras.models import Producto, Pedido, Lineapedido

class LineapedidoInline(admin.StackedInline):
    model = Lineapedido
    extra = 0


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','usuario','fecha']
    inlines = [LineapedidoInline]



admin.site.register(Producto)
admin.site.register(Pedido,PedidoAdmin)
