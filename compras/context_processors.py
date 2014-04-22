from django.shortcuts import get_object_or_404
from .models import Producto

from django.http import HttpResponse
import json as simplejson

def cart(request):
	llaves = request.session["llavesp"]
	if request.method=="POST":
		try:
			print("entro al try")
			id_producto = request.POST['product_id2']
			cant = request.POST['cantidad']
			veces = int(cant)
			print("#################################################################")
			print("#################################################################")
			print("#################################################################")
			print(llaves)
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
			print(llaves)

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

			p = get_object_or_404(Producto, pk=id_producto)
			mensajea = {"statusa":"True","product_id2":p.id, "nombrep":p.nombre, "rep":veces,}
			print(mensajea)
			request.session["llavesp"] = llaves
			return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')
		except:
			mensaje = {"statusa":"False"}
			return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')
		print("el producto NOOOOOOOOOOOOOOOOOOO esta en request post")
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



	zk = []
	for i in a:
		e = get_object_or_404(Producto, pk=i)
		zk.append(e)

	print("zk---------------------aaaaaaaaaaaaaaaa")
	print(zk)
	bu = len(canti)
	ctx = {'canti':canti,'zk':zk,'bu':bu}


	return ctx




def shopping(request):
	cosas = request.session["llavesp"]
	listado=[]
	precioscompra=[]
	for cosa in cosas:
		elemento = get_object_or_404(Producto, pk=cosa)
		#precioelemento = elemento.precioventa
		#precioscompra.append(precioelemento)
		listado.append(elemento)
		#totalapagar = sum(precioscompra)

	dict = {
		'listado':listado,
		#'totalapagar':totalapagar,
	}
	return dict