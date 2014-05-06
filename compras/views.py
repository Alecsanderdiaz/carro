#encoding:utf-8
from django.shortcuts import render, get_object_or_404
from .models import Producto, Pedido, Lineapedido
from django.http import HttpResponseRedirect, HttpResponse
import json as simplejson

def vaciarcarro(request):
	# vista creada para vaciar carro
	request.session["llavesp"] = []
	return render(request, 'vaciarcarro.html')

def home(request):

	# si hay una sesion nueva, inicio mi variable en cero
	# si la sesion existe, no realizo nada

	if "llavesp" in request.session:
		pass
	else:
		request.session["llavesp"] = []

	llaves = request.session["llavesp"]

	# si el metodo es post

	if request.method=="POST":
		# si se quiere agregar un producto o modificar la cantidad existente en el carrito
		if "product_id2" in request.POST:
			# obtengo el id del producto
			id_producto = request.POST['product_id2']
			a =unicode(id_producto)
			# obtengo la cantidad, deseada por el usuario
			cant = request.POST['cantidad']
			veces = int(cant)
			# obtengo la cantidad en inventario
			cantinv = request.POST['cantidad2']
			vecesinv = int(cantinv)
			# realizo la diferencia entre la cantidad en inventario y la requerida
			blue = vecesinv - veces

			# si la diferencia es mayor o igual a cero, significa que tenemos lo requerido
			if blue >= 0:
				# Realizo una excepcion
				try:
					# consulto la cantidad de productos que tengo en la variable de sesion
					# si se va a agregar por primera vez, la respuesta será cero
					ji = llaves.count(a)
					# hago una diferencia entre cantidad que quiero y la que existe en la sesión
					pu=veces-ji

					# si la diferencia es mayor que cero, agrego dicha difrencia
					if pu > 0:
						for i in range(pu):
							llaves.append(a)

					# si la diferencia es menor que cero, quito dicha diferencia
					if pu < 0:
						pua = abs(pu)
						for i in range(pua):
							llaves.remove(a)

					# si la diferencia es cero, dejo la variable de sesión igual
					if pu == 0:
						pass

					# obtengo una lista que contiene los elementos de la variable de sesion
					# sin repetirse
					a =set(llaves)
					# obtengo la cantidad de elemntos en la nueva lista, lo que se traduce en 
					# cuantos elementos hay en el carrito
					lo = len(a)

					# creo una nueva lista, que contendra la cantidad de productos en particular
					canti=[]
					for k in a:
						h=llaves.count(k)
						canti.append(h)

					# creo una nueva lista, que contendra los precios de los productos en particular
					precios = []
					for i in a:
						e = get_object_or_404(Producto, pk=i)
						pr = e.precio
						precios.append(pr)

					# obtengo una nueva lista que contiene los precios totales de los productos en particular
					xy = [i*j for (i,j) in zip(canti,precios)]

					# sumando los  elementos de la ultima lista, obtengo el total a pagar del cliente
					suma = sum(xy)
					# obtengo el subtotal
					st = int(suma/1.16)
					# obtengo el iva
					iv = int(suma-st)

					# obtengo el producto que se estaba modificando
					p = get_object_or_404(Producto, pk=id_producto)
					# Preparo el mensaje que se va enviar via json
					mensajea = {"statusa":"True","product_id2":p.id, "nombrep":p.nombre, "rep":veces,"lo":lo, "suma":suma}
					# modifico la variable de sesion
					request.session["llavesp"] = llaves
					return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')

				except:
					mensajea = {"statusa":"False"}
					return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')

			# si el cliente ha elegido una cantidad mayor a la que hay en inventario.
			else:
				mensajea = {"statusa":"False"}
				return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')

		else:
			# si hay metodo post, pero no es para agregar o modificar
			# significa que el cliente quiere eliminar un producto del carrito
			try:

				# averiguo el id del producto que se desea eliminar del  carrito
				id_producto = request.POST['product_id']
				a=unicode(id_producto)

				# obtengo la cantidad de productos en particular, que tengo en el carrito
				jo = llaves.count(a)
				# elimino de la variable de sesion, todos los id's del producto en particular
				for i in range(jo):
					llaves.remove(a)

				# obtengo el producto que  he eliminado
				p = get_object_or_404(Producto, pk=id_producto)
				# modifico la variable de sesion
				request.session["llavesp"] = llaves
				# obtengo una nueva lista de productos sin repetir
				a =set(llaves)
				# obtengo la cantidad de cada uno de los productos que estan en el carrito
				canti=[]
				for k in a:
					h=llaves.count(k)

				# obtengo los precios de cada uno de los productos en el carrito
				precios = []
				for i in a:
					e = get_object_or_404(Producto, pk=i)
					pr = e.precio
					precios.append(pr)

				# en una nueva lista obtengo el precio total de los productos en particular
				xy = [i*j for (i,j) in zip(canti,precios)]
				# obtengo el valor total, el subtotal y el iva de todo lo que hay en el  carrito				
				suma = sum(xy)
				st = int(suma/1.16)
				iv = int(suma-st)
				# obtengo la cantidad de productos particulares en el carro
				lo = len(xy)
				# preparo el mensaje con los datos que requiere el archivo eliminarcarro.js
				mensaje = {"statuse":"True","product_id":p.id, "suma":suma,"st":st,"iv":iv,"lo":lo}
				return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

			except:
				mensaje = {"statuse":"False"}
				return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

	# si no es metodo POST, solo tengo que mandar los productos que esten en la base de datos
	Productos = Producto.objects.all()
	return render(request,'index.html',{'Productos':Productos})

def pagina2(request):
	# vistas de prueba para los contextprocessors
	return render(request,'pagina2.html')

def pagina3(request):
	# vistas de prueba para los contextprocessors
	return render(request,'pagina3.html')

def carro(request):
	# si es una variable de sesion nueva, agrego una variable de sesion vacia
	# si la sesion existe, no realizo accion
	if "llavesp" in request.session:
		pass
	else:
		request.session["llavesp"] = []

	# le doy un nombre a la variable de sesion
	llaves = request.session["llavesp"]
	# si  el metodo es post
	if request.method=="POST":



		if "product_id2" in request.POST:
			# obtengo el id del producto
			id_producto = request.POST['product_id2']
			a =unicode(id_producto)
			# obtengo la cantidad, deseada por el usuario
			cant = request.POST['cantidad']
			veces = int(cant)
			# obtengo la cantidad en inventario
			cantinv = request.POST['cantidad2']
			vecesinv = int(cantinv)
			# realizo la diferencia entre la cantidad en inventario y la requerida
			blue = vecesinv - veces
			print(blue)

			# si la diferencia es mayor o igual a cero, significa que tenemos lo requerido
			if blue >= 0:
				try:
					# obtengo la cantidad de productos con ese id,  que ya hay en el carro
					ji = llaves.count(a)
					# obtengo la diferencia entre la cantidad que se desea, y la que ya se se tenia
					pu=veces-ji
					# si la diferencia es positiva, agrego dicha diferencia, en la variable de sesion
					if pu > 0:
						for i in range(pu):
							llaves.append(a)

					# si la diferencia es negativa, remuevo dicha diferencia de la variable de sesion
					if pu < 0:
						pua = abs(pu)
						for i in range(pua):
							llaves.remove(a)

					# si la diferencia es cero, no agrego, ni elimino
					if pu == 0:
						pass

					# obtengo el producto que estoy modificando
					p = get_object_or_404(Producto, pk=id_producto)
					# obtengo el precio de dicho producto
					precio1 = p.precio
					# obtengo el precio total de la cantidad del producto en cuestion
					preciot = precio1*veces
					# modifico la variable de sesion
					request.session["llavesp"] = llaves
					# obtengo una lista con los id's de los productos en el carrito, sin repetir
					a =set(llaves)
					# para la anterior lista, creo una lista paralela que contiene la cantidad de cada
					# uno de los prodctos
					canti=[]
					for k in a:
						h=llaves.count(k)
						canti.append(h)

					# obtengo una lista con los precios unitarios de los productos
					precios = []
					for i in a:
						e = get_object_or_404(Producto, pk=i)
						pr = e.precio
						precios.append(pr)

					# obtengo una lista con los precios totales, de los productos en particular
					xy = [i*j for (i,j) in zip(canti,precios)]
					# obtengo el total a pagar, el subtotal y el iva de la compra realizada
					suma = sum(xy)
					st = int(suma/1.16)
					iv = int(suma-st)
					# obtengo la cantidad de productos particulares en el carro
					lo = len(xy)
					# preparo el mensaje que retorno a agregarcarro.js
					mensajea = {"statusa":"True","product_id2":p.id, "nombrep":p.nombre, "rep":veces, "preciot":preciot, "suma":suma,"st":st,"iv":iv, "lo":lo}
					return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')

				except:
					mensajea = {"statusa":"False"}
					return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')
			# si no tenemos en inventario la cantiidad deseada por el cliente, mandamos una alerta
			else:
				mensajea = {"statusa":"False"}
				return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')

		else:
			# si no deseamos modificar la cantidad, lo que deseamos es eliminar el producto particular
			try:
				# obtengo el id del producto a eliminar
				id_producto = request.POST['product_id']
				a=unicode(id_producto)
				# obtengo la cantidad de productos que tenia la variable de sesion
				jo = llaves.count(a)
				# elimino dicha cantidad
				for i in range(jo):
					llaves.remove(a)
				
				# obtengo el producto en particular
				p = get_object_or_404(Producto, pk=id_producto)
				# modifico la variable de sesion
				request.session["llavesp"] = llaves
				# obtengo una lista con los id's sin repetir
				a =set(llaves)
				# para cada id de la anterior lista, encuentro la cantidad en particular en la variable de sesion
				canti=[]
				for k in a:
					h=llaves.count(k)
					canti.append(h)

				# obtengo los precios unitarios de los productos particulares del carrito
				precios = []
				for i in a:
					e = get_object_or_404(Producto, pk=i)
					pr = e.precio
					precios.append(pr)

				# obtengo los precios totales de los productos particulaes del carrito
				xy = [i*j for (i,j) in zip(canti,precios)]
				# obtengo total a pagar, iva y subtotal
				suma = sum(xy)
				st = int(suma/1.16)
				iv = int(suma-st)
				# obtengo la cantidad de productos particulares en el carrito
				lo = len(xy)
				# preparo el mensaje json que mando a liminarcarrro.js
				mensaje = {"statuse":"True","product_id":p.id, "suma":suma,"st":st,"iv":iv,"lo":lo}
				return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
			except:
				mensaje = {"statuse":"False"}
				return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')

	# si el metodo no es post

	# obtengo una lista que hereda de la variable de sesion
	# pero no contiene id's repetidos
	a =set(llaves)

	# obtengo tres listas una con cantidades, precios unitarios y los productos particulares en el carrito
	canti=[]
	precios = []
	zk = []
	for i in a:
		h=llaves.count(i)
		canti.append(h)
		e = get_object_or_404(Producto, pk=i)
		zk.append(e)
		pr = e.precio
		precios.append(pr)

	# obtengo los precios totales de los productos particulares
	xy = [i*j for (i,j) in zip(canti,precios)]
	# obtengo total a pagar, subtotal e IVA
	suma = sum(xy)
	st = int(suma/1.16)
	iv = int(suma-st)


	return render(request, 'carro.html',{'canti':canti,'zk':zk,'xy':xy,'suma':suma,'st':st,'iv':iv})


def mandarpedido(request):
	# si es una variable de sesion nueva, agrego una variable de sesion vacia
	# si la sesion existe, no realizo accion
	if "llavesp" in request.session:
		pass
	else:
		request.session["llavesp"] = []

	llaves = request.session["llavesp"]

	# obtengo una lista con id's particulares sin repetir
	a =set(llaves)
	# obtengo las cantidades de dichos productos particulares
	canti=[]
	for k in a:
		h=llaves.count(k)
		canti.append(h)

	# creo un pedido en la base de datos
	ped = Pedido.objects.create(usuario=request.user)
	# en la base de datos modifico el stock y creo lineas de pedido para el pedido
	# creado en la anterior linea de codigo
	for x, y in zip(a, canti):
		e = get_object_or_404(Producto, pk=x)
		e.stock -= y 
		e.save()
		o = Lineapedido.objects.create(productop=e,pedidoid=ped,cantidad=y)

	# Despues de crear el pedido, vuelvo mi variable de sesion a cero y redirijo a inicio
	request.session["llavesp"] = []
	return HttpResponseRedirect('/inicio')



from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


def ingresar(request):
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/inicio')
				else:
					return render(request, 'index.html')
			else:
				return render(request,'index.html')
	else:
		formulario = AuthenticationForm()
	return render(request,'ingresar.html',{'formulario':formulario})

def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/inicio')

def buscar(request):
	# vistas de busqueda
	if request.method == 'POST':
		buscar = request.POST['buscalo']
		productob = Producto.objects.filter(nombre__contains=buscar)

	return render(request,'buscar.html',{'productob':productob})	