from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from registroAsociado.forms import *
from django.views.generic import ListView, CreateView
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def crearEjecutivo(request):	
	if request.method == 'GET':
		form = EjecutivoForm()
	else:
		form = EjecutivoForm(request.POST)
		if form.is_valid():			
			form.save()
		return redirect('registrarEjecutivo')
	return render(request, 'ejecutivos/registrarEjecutivo.html', {'form':form})


def ListEjecutivo(request):
	if request.method =='GET':
		ejecutivos= ejecutivo.objects.all().order_by('-idEjecutivo')	
		contexto={'ejecutivos':ejecutivos}
	else:
		return redirect('verEjecutivo')
	return render(request, 'ejecutivos/verEjecutivo.html', contexto)
	

def crearCliente(request):	
	if request.method == 'GET':
		form1 = clienteForm()
	else:
		form1 = clienteForm(request.POST)
		if form1.is_valid():			
			client = form1.save()
			return redirect('crearBeneficiario',client.idCliente)
		return redirect('registrarCliente')
	return render(request, "clientes/registrarCliente.html", {'form': form1})

def ListCliente(request):
	if request.method =='GET':
		clientes= cliente.objects.all().order_by('-idCliente')	
		contexto={'clientes':clientes}
	else:
		return redirect('verCliente')
	return render(request, 'clientes/verCliente.html', contexto)
	
def updateCliente(request, idCliente):
	clientes = cliente.objects.get(idCliente = idCliente)
	if request.method == 'GET':
		form = clienteForm(instance=clientes)
	else:
		form = clienteForm(request.POST, instance=clientes)
		if form.is_valid():
			form.save()			
		return redirect('verCliente')
	return render(request, 'clientes/registrarCliente.html', {'form':form})


def crearBeneficiario(request, idCliente):	
	if request.method == 'GET':
		form = beneficiariosForm()
	else:
		form = beneficiariosForm(request.POST)
		if form.is_valid():		
			obj3 = form.save(commit=False)
			obj3.clienteBeneficiario = cliente.objects.get(pk=idCliente)
			form.save()
			return redirect('crearBeneficiario2',idCliente)
	return render(request, 'beneficiarios/registrarBeneficiario.html', {'form':form})

def crearBeneficiario2(request, idCliente):	
	if request.method == 'GET':
		form = beneficiariosForm()
	else:
		form = beneficiariosForm(request.POST)
		if form.is_valid():		
			obj3 = form.save(commit=False)
			obj3.clienteBeneficiario = cliente.objects.get(pk=idCliente)
			form.save()
			return redirect('crearReferencias',idCliente)
	return render(request, 'beneficiarios/registrarBeneficiario.html', {'form':form})

def crearReferencias(request, idCliente):	
	if request.method == 'GET':
		form = refereciasForm()
	else:
		form = refereciasForm(request.POST)
		if form.is_valid():		
			obj3 = form.save(commit=False)
			obj3.cliente_idCliente3 = cliente.objects.get(pk=idCliente)
			form.save()
			return redirect('crearReferencias2',idCliente)
	return render(request, 'referencias/registrarReferencia.html', {'form':form})

def inicioSesion(request):
	return render(request,'inicioSesion/inicioSesion.html',{
		'inicio' : UserCreationForm
	})

def crearReferencias2(request, idCliente):	
	if request.method == 'GET':
		form = refereciasForm()
	else:
		form = refereciasForm(request.POST)
		if form.is_valid():		
			obj3 = form.save(commit=False)
			obj3.cliente_idCliente3 = cliente.objects.get(pk=idCliente)
			form.save()
			return redirect('crearReferencias3',idCliente)
	return render(request, 'referencias/registrarReferencia.html', {'form':form})

def crearReferencias3(request, idCliente):	
	if request.method == 'GET':
		form = refereciasForm()
	else:
		form = refereciasForm(request.POST)
		if form.is_valid():		
			obj3 = form.save(commit=False)
			obj3.cliente_idCliente3 = cliente.objects.get(pk=idCliente)
			form.save()
			return redirect('crearReferencias4',idCliente)
	return render(request, 'referencias/registrarReferencia.html', {'form':form})

def crearReferencias4(request, idCliente):	
	if request.method == 'GET':
		form = refereciasForm()
	else:
		form = refereciasForm(request.POST)
		if form.is_valid():		
			obj3 = form.save(commit=False)
			obj3.cliente_idCliente3 = cliente.objects.get(pk=idCliente)
			form.save()
			return redirect('crearTrabajo', idCliente)
	return render(request, 'referencias/registrarReferencia.html', {'form':form})


def crearTrabajo(request, idCliente):	
	if request.method == 'GET':
		form = trabajosForm()
	else:
		form = trabajosForm(request.POST)
		if form.is_valid():		
			obj3 = form.save(commit=False)
			obj3.cliente_idCliente = cliente.objects.get(pk=idCliente)
			form.save()
			return redirect('crearDocumentos', idCliente)
	return render(request, 'trabajos/registrarTrabajo.html', {'form':form})

def crearDocumentos(request, idCliente):	
	if request.method == 'GET':
		form = documentosForm()
	else:
		form = documentosForm(request.POST)
		if form.is_valid():		
			obj3 = form.save(commit=False)
			obj3.cliente_idCliente = cliente.objects.get(pk=idCliente)
			form.save()
			return redirect('crearAsociacion', idCliente)
	return render(request, 'documentos/registrarDocumentos.html', {'form':form})

def crearAsociacion(request, idCliente):	
	if request.method == 'GET':
		form = asociacionForm()
	else:
		form = asociacionForm(request.POST)
		if form.is_valid():		
			obj3 = form.save(commit=False)
			obj3.cliente_idCliente = cliente.objects.get(pk=idCliente)
			form.save()
			return redirect('generarContrato', idCliente)
	return render(request, 'asociacion/registrarAsociacion.html', {'form':form})

def generarContrato(request, idCliente):	
	buf = io.BytesIO()
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont('Helvetica', 11)
	
	lines = [ 
		"Asociación Cooperativa de Ahorro ",
		"Crédito Consumo y Aprovisionamiento de los Miembros de la Comunidad y ",
		"Corporación de la Universidad de El Salvador de ",
		"Responsabilidad Limitada Presente", 
		" ",
		"Por este medio solicito se me admita como asociado de su cooperativa, así mismo manifiesto",
		"que me obligo a cumplir con lo dispuesto en la Ley General de Asociaciones Cooperativas ",
		"su Reglamento. Estatutos y Reglamentos Internos de la Cooperativa, asi como enmiendas que a futuro ",
		"se les hicieran y todas aquellas disposiciones legales y administrativas de interés para la cooperativa",
		" ",
		"DATOS GENERALES",
		" ",
		]
	clienteSolicitud = cliente.objects.get(pk=idCliente)
	documentosCliente = catalogoDocumentos.objects.get(cliente_idCliente_id=idCliente)
	trabajoliente = trabajo.objects.get(cliente_idCliente=idCliente)
	lines.append("Nombre Completo:"+ clienteSolicitud.primerNombre + " " + clienteSolicitud.segundoNombre + " " + clienteSolicitud.primerApellido + " " + clienteSolicitud.segundoApellido)
	lines.append("DUI:" + documentosCliente.numDocumento)
	lines.append("Fecha de nacimiento: " + clienteSolicitud.fechaNacimiento)
	lines.append("Nacionalidad: " + clienteSolicitud.nacionalidad)
	lines.append("Pais de nacimiento: " + clienteSolicitud.paisNacimiento)
	lines.append("Capacidad de pago: $" + trabajoliente.capacidadPago)
	lines.append(' ')
	lines.append("Beneficiarios: ")
	beneficiariosCliente = beneficiario.objects.all()
	for ben in beneficiariosCliente:
		lines.append(' ')
		lines.append('Nombres: ' + ben.nombreBeneficiario)
		lines.append('Apellidos: ' + ben.apellidoBeneficiario)
		lines.append('Telefono: ' + ben.telBeneficiario)
		lines.append('Edad: ' +  str(ben.edadBeneficiario))
		lines.append('Parentesco: ' + ben.parenscoBeneficiario)
		lines.append('Porcentaje: ' + str(ben.porcentajeBeneficiario) +'%')
		

	for line in lines: 
		textob.textLine(line)
	
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	return FileResponse(buf, as_attachment=True, filename='contract.pdf')
