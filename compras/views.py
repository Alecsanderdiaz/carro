from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.http import HttpResponseRedirect, HttpResponse
import json as simplejson

def vaciarcarro(request):
	request.session["llavesp"] = []
	return render(request, 'vaciarcarro.html')

def home(request):

	llaves = request.session["llavesp"]

	# if request.method=="POST":
	# 	print("si hay metodo post")
	# 	if "product_id2" in request.POST:
	# 		print("el producto esta en request post")
	# 		try:
	# 			print("entro al try")
	# 			id_producto = request.POST['product_id2']
	# 			print(id_producto)
	# 			a=unicode(id_producto)
	# 			llaves.append(a)
	# 			p = get_object_or_404(Producto, pk=id_producto)
	# 			mensajea = {"statusa":"True","product_id2":p.id}
	# 			print(mensajea)
	# 			request.session["llavesp"] = llaves
	# 			return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')
	# 		except:
	# 			mensaje = {"statusa":"False"}
	# 			return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')
	# 	print("el producto NOOOOOOOOOOOOOOOOOOO esta en request post")

	if request.method=="POST":
		print("si hay metodo post")
		print("el producto esta en request post")
		try:
			print("entro al try")
			id_producto = request.POST['product_id2']
			cant = request.POST['cantidad']
			print("#################################################################")
			print(request.POST)
			print("#################################################################")
			#print(id_producto1)
			veces = int(cant)
			print(veces)
			for i in range(veces):
				print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
				print(i)
				a=unicode(id_producto)
				llaves.append(a)
			p = get_object_or_404(Producto, pk=id_producto)
			mensajea = {"statusa":"True","product_id2":p.id, "nombrep":p.nombre, "rep":veces,}
			print(mensajea)
			request.session["llavesp"] = llaves
			return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')
		except:
			mensaje = {"statusa":"False"}
			return HttpResponse(simplejson.dumps(mensajea),content_type='application/json')
		print("el producto NOOOOOOOOOOOOOOOOOOO esta en request post")

	Productos = Producto.objects.all()
	return render(request,'index.html',{'Productos':Productos})

def pagina2(request):
	return render(request,'pagina2.html')

def pagina3(request):
	return render(request,'pagina3.html')

def carro(request):


	llaves = request.session["llavesp"]

	if request.method=="POST":
		print("###############################Ha entrado al POST")
		if "product_id" in request.POST:
			print("###############################Entro al if")
			try:
				print("###############################entro al try")
				id_producto = request.POST['product_id']
				print("---------------------------------------id_producto")
				print(id_producto)
				#llaves = request.session["llavesp"]
				print("---------------------------------------llaves")
				print(request.session["llavesp"])
				a=unicode(id_producto)
				print("---------------------------------------a")
				print(a)
				llaves.remove(a)
				print("---------------------------------------llavesremove")
				print(request.session["llavesp"])
				print("---------------------------------------u'id_producto'")
				print(id_producto)

				p = get_object_or_404(Producto, pk=id_producto)
				#p = producto.objects.get(pk=id_producto)
				#print("---------------------------------------p")
				print(p)
				mensaje = {"statuse":"True","product_id":p.id}
				print(mensaje)
				request.session["llavesp"] = llaves
				#p.delete() # Elinamos objeto de la base de datos
				print("###############################antes retur del try")
				print("salio try")
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



	zk = []
	for i in a:
		e = get_object_or_404(Producto, pk=i)
		zk.append(e)

	print("zk---------------------aaaaaaaaaaaaaaaa")
	print(zk)


	return render(request, 'carro.html',{'canti':canti,'zk':zk})


def alcarrito(request, p_id):
	p = get_object_or_404(Producto, pk=p_id)
	llaves = request.session["llavesp"]
	llaves.append(p_id)
	print(llaves)
	request.session["llavesp"] = llaves

	return HttpResponseRedirect("/inicio")