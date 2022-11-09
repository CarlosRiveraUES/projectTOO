from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from registroAsociado.forms import *
from django.views.generic import ListView, CreateView
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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
	

def UpdateEjecutivo(request, ejecutivoID):
	ejecutivos = ejecutivo.objects.get(idEjecutivo = ejecutivoID)
	if request.method == 'GET':
		form = EjecutivoForm(instance=ejecutivos)
	else:
		form = EjecutivoForm(request.POST, instance=ejecutivos)
		if form.is_valid():
			form.save()			
		return redirect('verEjecutivo')
	return render(request, 'ejecutivos/registrarEjecutivo.html', {'form':form})


def crearCliente(request):	
	if request.method == 'GET':
		form = clienteForm()
	else:
		form = clienteForm(request.POST)
		if form.is_valid():			
			client = form.save()
			return redirect('crearBeneficiario',client.idCliente)
		return redirect('registrarCliente')
	return render(request, 'clientes/registrarCliente.html', {'form':form})

def ListCliente(request):
	if request.method =='GET':
		clientes= cliente.objects.all().order_by('-idCliente')	
		contexto={'clientes':clientes}
	else:
		return redirect('verCliente')
	return render(request, 'clientes/verCliente.html', contexto)
	
def UpdateCliente(request, idClientes):
	clientes = cliente.objects.get(idCliente = idClientes)
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
		return render(request, 'beneficiarios/registrarBeneficiario.html', {'form':form})
	return render(request, 'beneficiarios/registrarBeneficiario.html', {'form':form})

def inicioSesion(request):
	return render(request,'inicioSesion/inicioSesion.html',{
		'inicio' : UserCreationForm
	})