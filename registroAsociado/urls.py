from django.urls import path
from registroAsociado.views import * 

urlpatterns = [
	path('ejecutivo', ListEjecutivo, name="verEjecutivo"),
	path('ejecutivoAgregar', crearEjecutivo, name="registrarEjecutivo"),	
	path('modificar/<int:ejecutivoID>', UpdateEjecutivo, name="updateEjecutivo"),
	# path('transaccion/agregar', CreateTransaccion, name="registrarTransaccion"),	

	path('cliente', ListCliente, name="verCliente"),
	path('clienteAgregar', crearCliente, name="registrarCliente"),	
	path('modificar/<int:idCliente>', UpdateCliente, name="updateCliente"),

	path('registrarBeneficiarios/<int:idCliente>', crearBeneficiario, name="crearBeneficiario"),
	
	
    
]

