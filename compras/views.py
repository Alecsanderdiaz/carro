from django.shortcuts import render, get_object_or_404
from .models import Producto, Pedido, Lineapedido
from django.http import HttpResponseRedirect, HttpResponse
import json as simplejson

def vaciarcarro(request):
	request.session["llavesp"] = []
	return render(request, 'vaciarcarro.html')

def home(request):

	if "llavesp" in request.session:
		pass
	else:
		request.session["llavesp"] = []

	print("hola2")
	llaves = request.session["llavesp"]
	if request.method=="POST":
		if "product_id2" in request.POST:
			try:
				print("#################-MODIFICAR-HOME-##################################")
				id_producto = request.POST['product_id2']
				cant = request.POST['cantidad']
				veces = int(cant)
				print("#################################################################")
				print("#################################################################")
				print("#################################################################")
				#print(llaves)
				a =unicode(id_producto)
				print("#########################count###################################")
				ji = llaves.count(a)
				print(ji)
				pu=veces-ji
				print("#########################pu######################################")
				print(pu)

				if pu > 0:
					for i in range(pu):
						llaves.append(a)
				#print("#################################################################")
				#print(llaves)

				if pu < 0:
					pua = abs(pu)
					for i in range(pua):
						llaves.remove(a)

				if pu == 0:
					pass


				# if a in llaves:
				# 	for q in llaves:
				# 		llaves.remove(a)
				# print("#################################################################")
				# print(llaves)



				# a =set(llaves)
				# print("############################SET##################################")
				# print(a)

				# canti=[]
				# for k in a:
				# 	h=llaves.count(k)
				# 	canti.append(h)
				# print("############################CANTI################################")
				# print(canti)
				a =set(llaves)
				lo = len(a)

				a =set(llaves)
				print("set---------------------aaaaaaaaaaaaaaaa")
				print(a)

				canti=[]
				for k in a:
					h=llaves.count(k)
					canti.append(h)
				print("canti--------------------aaaaaaaaaaaaaaaa")
				print(canti)


				precios = []
				zk = []
				for i in a:
					e = get_object_or_404(Producto, pk=i)
					zk.append(e)
					pr = e.precio
					precios.append(pr)

				xy = [i*j for (i,j) in zip(canti,precios)]
				print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
				print(xy)



				print("zk---------------------aaaaaaaaaaaaaaaa")
				print(zk)

				suma = sum(xy)
				print(suma)
				st = int(suma/1.16)
				print(st)
				iv = int(suma-st)
				print(iv)

				lo = len(xy)

				p = get_object_or_404(Producto, pk=id_producto)
				mensajea = {"statusa":"True","product_id2":p.id, "nombrep":p.nombre, "rep":veces,"lo":lo, "suma":suma}
				print(mensajea)
				request.session["llavesp"] = llaves
				return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')
			except:
				mensaje = {"statusa":"False"}
				return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')
			print("el producto NOOOOOOOOOOOOOOOOOOO esta en request post")

		else:
			print("hay un producto product_id")
			try:
				print("#################-ELIMINAR-HOME-##################################")
				id_producto = request.POST['product_id']
				cantida = request.POST['cantidade']
				print("---------------------------------------id_producto")
				print(id_producto)
				print("---------------------------------------cantida")
				print(cantida)
				#llaves = request.session["llavesp"]
				print("---------------------------------------llaves")
				#print(request.session["llavesp"])
				a=unicode(id_producto)
				print("---------------------------------------a")
				print(a)
				jo = llaves.count(a)
				for i in range(jo):
					llaves.remove(a)
				print("---------------------------------------llavesremove")
				#print(request.session["llavesp"])
				print("---------------------------------------u'id_producto'")
				print(id_producto)
##
				
				p = get_object_or_404(Producto, pk=id_producto)


				print(llaves)
				request.session["llavesp"] = llaves

#
				li = []
				for i in request.session["llavesp"]:
					e = get_object_or_404(Producto, pk=i)
					li.append(e)


				a =set(llaves)
				print("set---------------------aaaaaaaaaaaaaaaa")
				print(a)

				canti=[]
				for k in a:
					h=llaves.count(k)
					canti.append(h)
				print("canti--------------------aaaaaaaaaaaaaaaa")
				print(canti)


				precios = []
				zk = []
				for i in a:
					e = get_object_or_404(Producto, pk=i)
					zk.append(e)
					pr = e.precio
					precios.append(pr)

				xy = [i*j for (i,j) in zip(canti,precios)]
				print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
				print(xy)



				print("zk---------------------aaaaaaaaaaaaaaaa")
				print(zk)

				suma = sum(xy)
				print(suma)
				st = int(suma/1.16)
				print(st)
				iv = int(suma-st)
				print(iv)

				lo = len(xy)

#

				mensaje = {"statuse":"True","product_id":p.id, "suma":suma,"st":st,"iv":iv,"lo":lo}
				print(mensaje)


##

				##p = get_object_or_404(Producto, pk=id_producto)

				##mensaje = {"statuse":"True","product_id":p.id}

				print("###############################antes retur del try")

				return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
				#print("salio try")
			except:
				print("###############################entro except")
				mensaje = {"statuse":"False"}
				print("###############################antes retur del except")
				return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
				print("salio del except")


	Productos = Producto.objects.all()
	return render(request,'index.html',{'Productos':Productos})

def pagina2(request):
	return render(request,'pagina2.html')

def pagina3(request):
	return render(request,'pagina3.html')

def carro(request):

	if "llavesp" in request.session:
		pass
	else:
		request.session["llavesp"] = []


	llaves = request.session["llavesp"]

	if request.method=="POST":
		print("hay request en la vista carro")
		if "product_id2" in request.POST:
			print("hay un producto product_id2")
			try:
				print("#################-MODIFICAR-CARRO-##################################")
				id_producto = request.POST['product_id2']
				cant = request.POST['cantidad']
				veces = int(cant)
				print("#################################################################")
				print("#################################################################")
				print("#################################################################")
				#print(llaves)
				a =unicode(id_producto)
				print("#########################count###################################")
				ji = llaves.count(a)
				print(ji)
				pu=veces-ji
				print("#########################pu######################################")
				print(pu)

				if pu > 0:
					for i in range(pu):
						llaves.append(a)
				print("#################################################################")
				#print(llaves)

				if pu < 0:
					pua = abs(pu)
					for i in range(pua):
						llaves.remove(a)

				if pu == 0:
					pass


				# if a in llaves:
				# 	for q in llaves:
				# 		llaves.remove(a)
				# print("#################################################################")
				# print(llaves)



				# a =set(llaves)
				# print("############################SET##################################")
				# print(a)

				# canti=[]
				# for k in a:
				# 	h=llaves.count(k)
				# 	canti.append(h)
				# print("############################CANTI################################")
				# print(canti)

#

				p = get_object_or_404(Producto, pk=id_producto)
				precio1 = p.precio
				preciot = precio1*veces

				print(llaves)
				request.session["llavesp"] = llaves

#
				li = []
				for i in request.session["llavesp"]:
					e = get_object_or_404(Producto, pk=i)
					li.append(e)


				a =set(llaves)
				print("set---------------------aaaaaaaaaaaaaaaa")
				print(a)

				canti=[]
				for k in a:
					h=llaves.count(k)
					canti.append(h)
				print("canti--------------------aaaaaaaaaaaaaaaa")
				print(canti)


				precios = []
				zk = []
				for i in a:
					e = get_object_or_404(Producto, pk=i)
					zk.append(e)
					pr = e.precio
					precios.append(pr)

				xy = [i*j for (i,j) in zip(canti,precios)]
				print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
				print(xy)



				print("zk---------------------aaaaaaaaaaaaaaaa")
				print(zk)

				suma = sum(xy)
				st = int(suma/1.16)
				iv = int(suma-st)

				lo = len(xy)

#

				mensajea = {"statusa":"True","product_id2":p.id, "nombrep":p.nombre, "rep":veces, "preciot":preciot, "suma":suma,"st":st,"iv":iv, "lo":lo}
				print(mensajea)


#
				return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')
			except:
				mensaje = {"statusa":"False"}
				return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')

		else:
			print("hay un producto product_id")
			try:
				print("#################-ELIMINAR-CARRO-##################################")
				id_producto = request.POST['product_id']
				cantida = request.POST['cantidade']
				print("---------------------------------------id_producto")
				print(id_producto)
				print("---------------------------------------cantida")
				print(cantida)
				#llaves = request.session["llavesp"]
				print("---------------------------------------llaves")
				#print(request.session["llavesp"])
				a=unicode(id_producto)
				print("---------------------------------------a")
				print(a)
				jo = llaves.count(a)
				for i in range(jo):
					llaves.remove(a)
				print("---------------------------------------llavesremove")
				#print(request.session["llavesp"])
				print("---------------------------------------u'id_producto'")
				print(id_producto)
##
				
				p = get_object_or_404(Producto, pk=id_producto)


				print(llaves)
				request.session["llavesp"] = llaves

#
				li = []
				for i in request.session["llavesp"]:
					e = get_object_or_404(Producto, pk=i)
					li.append(e)


				a =set(llaves)
				print("set---------------------aaaaaaaaaaaaaaaa")
				print(a)

				canti=[]
				for k in a:
					h=llaves.count(k)
					canti.append(h)
				print("canti--------------------aaaaaaaaaaaaaaaa")
				print(canti)


				precios = []
				zk = []
				for i in a:
					e = get_object_or_404(Producto, pk=i)
					zk.append(e)
					pr = e.precio
					precios.append(pr)

				xy = [i*j for (i,j) in zip(canti,precios)]
				print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
				print(xy)



				print("zk---------------------aaaaaaaaaaaaaaaa")
				print(zk)

				suma = sum(xy)
				print(suma)
				st = int(suma/1.16)
				print(st)
				iv = int(suma-st)
				print(iv)

				lo = len(xy)

#

				mensaje = {"statuse":"True","product_id":p.id, "suma":suma,"st":st,"iv":iv,"lo":lo}
				print(mensaje)


##

				##p = get_object_or_404(Producto, pk=id_producto)

				##mensaje = {"statuse":"True","product_id":p.id}

				print("###############################antes retur del try")

				return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
				#print("salio try")
			except:
				print("###############################entro except")
				mensaje = {"statuse":"False"}
				print("###############################antes retur del except")
				return HttpResponse(simplejson.dumps(mensaje),content_type='application/json')
				print("salio del except")






	
	li = []
	for i in request.session["llavesp"]:
		e = get_object_or_404(Producto, pk=i)
		li.append(e)


	a =set(llaves)
	print("set---------------------aaaaaaaaaaaaaaaa")
	print(a)

	canti=[]
	for k in a:
		h=llaves.count(k)
		canti.append(h)
	print("canti--------------------aaaaaaaaaaaaaaaa")
	print(canti)


	precios = []
	zk = []
	for i in a:
		e = get_object_or_404(Producto, pk=i)
		zk.append(e)
		pr = e.precio
		precios.append(pr)

	xy = [i*j for (i,j) in zip(canti,precios)]
	print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
	print(xy)



	print("zk---------------------aaaaaaaaaaaaaaaa")
	print(zk)

	suma = sum(xy)
	st = int(suma/1.16)
	iv = int(suma-st)


	return render(request, 'carro.html',{'canti':canti,'zk':zk,'xy':xy,'suma':suma,'st':st,'iv':iv})


def alcarrito(request, p_id):

	if "llavesp" in request.session:
		pass
	else:
		request.session["llavesp"] = []

	p = get_object_or_404(Producto, pk=p_id)
	llaves = request.session["llavesp"]
	llaves.append(p_id)
	print(llaves)
	request.session["llavesp"] = llaves

	return HttpResponseRedirect("/inicio")

def mandarpedido(request):

	if "llavesp" in request.session:
		pass
	else:
		request.session["llavesp"] = []

	llaves = request.session["llavesp"]

	a =set(llaves)
	print(a)

	canti=[]
	for k in a:
		h=llaves.count(k)
		canti.append(h)
	print(canti)
	ped = Pedido.objects.create(usuario=request.user)
	for x, y in zip(a, canti):
		e = get_object_or_404(Producto, pk=x)
		o = Lineapedido.objects.create(productop=e,pedidoid=ped,cantidad=y)

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