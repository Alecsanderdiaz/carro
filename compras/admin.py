from django.contrib import admin

# Register your models here.

from compras.models import Producto, Pedido, Lineapedido

class LineapedidoInline(admin.StackedInline):
    model = Lineapedido


class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','usuario','fecha']
    inlines = [LineapedidoInline]



admin.site.register(Producto)
admin.site.register(Pedido,PedidoAdmin)
	




# class RepuestoInline(admin.StackedInline):
#     model = Repuesto
#     extra = 3

# class ProductoAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Producto', {'fields': ['articulo', 'marca', 'referencia']}),
#         ('Inventario', {'fields': ['cantidad']}),
#         ('Dimensiones y Peso', {'fields': ['largo', 'ancho', 'alto', 'peso']}),
#         ('Precios', {'fields': ['preciocompra', 'precioventa', 'preciopromocion']}),
#     ]
#     inlines = [RepuestoInline]