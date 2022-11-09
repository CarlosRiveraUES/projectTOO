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
	path('registrarBeneficiarios2/<int:idCliente>', crearBeneficiario2, name="crearBeneficiario2"),

	path('registrarReferencias/<int:idCliente>', crearReferencias, name="crearReferencias"),
	path('registrarReferencias2/<int:idCliente>', crearReferencias2, name="crearReferencias2"),
	path('registrarReferencias3/<int:idCliente>', crearReferencias3, name="crearReferencias3"),
	path('registrarReferencias4/<int:idCliente>', crearReferencias4, name="crearReferencias4"),

	path('registrarTrabajo/<int:idCliente>', crearTrabajo, name="crearTrabajo"),
    
]

