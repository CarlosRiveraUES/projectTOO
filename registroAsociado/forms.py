from django import forms
from registroAsociado.models import *
from django.contrib.admin.widgets import AdminDateWidget

errores = {
    'required': 'Este campo es obligatorio',
    'invalid': 'El dato ingresado no es valido'
}

class EjecutivoForm(forms.ModelForm):
	class Meta:
		model = ejecutivo
		fields = '__all__'

		labels = {
        'nombreEjecutivo': 'Nombres',
        'apellidoEjecutivo':'Apellidos'
		}

		widgets= {
        'nombreEjecutivo': forms.TextInput(attrs={'class':'form-control'}),
        'apellidoEjecutivo': forms.TextInput(attrs={'class':'form-control'})
		}

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'
        labels = {
            'primerNombre': 'Primer nombre:',
            'segundoNombre': 'Segundo nombre:',
            'primerApellido': 'Primer apellido:',
            'segundoApellido': 'Segundo apellido:',
            'apellidoCasada': 'Apellido casada:',
            'fechaNacimiento': 'Fecha nacimiento:',
            'nacionalidad': 'Nacionalidad:',
            'paisNacimiento': 'Pais Nacimiento:',
            'ubicacion': 'Ubicacion:',
            'subRegion': 'Subregion:',
            'estadoCivil': 'Estado civil:',
            'genero_idGenero': 'Genero:'
        }
        widgets = {
          'primerNombre': forms.TextInput(attrs={'class': 'form-control'}),
          'segundoNombre': forms.TextInput(attrs={'class': 'form-control'}),
          'primerApellido': forms.TextInput(attrs={'class': 'form-control'}),
          'segundoApellido': forms.TextInput(attrs={'class': 'form-control'}),
          'apellidoCasada': forms.TextInput(attrs={'class': 'form-control'}),
          'fechaNacimiento': forms.TextInput(attrs={'class': 'form-control'}),
          'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
          'paisNacimiento': forms.TextInput(attrs={'class': 'form-control'}),
          'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
          'subRegion': forms.TextInput(attrs={'class': 'form-control'}),
          'estadoCivil': forms.Select(attrs={'class': 'form-control'}),
          'genero_idGenero': forms.Select(attrs={'class': 'form-control'}),
        }

class beneficiariosForm(forms.ModelForm):
    class Meta:
        model = beneficiario
        fields = ['nombreBeneficiario', 'apellidoBeneficiario', 'telBeneficiario', 'edadBeneficiario', 'parenscoBeneficiario', 'porcentajeBeneficiario']
        labels = {
            'nombreBeneficiario': 'Nombres:',
            'apellidoBeneficiario': 'Apellidos:',
            'telBeneficiario': 'Telefono:',
            'edadBeneficiario': 'Edad:',
            'parenscoBeneficiario': 'Parentesco:',
            'porcentajeBeneficiario': 'Porcentaje'
        }
        widgets = {
          'nombreBeneficiario': forms.TextInput(attrs={'class': 'form-control'}),
          'apellidoBeneficiario': forms.TextInput(attrs={'class': 'form-control'}),
          'telBeneficiario': forms.TextInput(attrs={'class': 'form-control'}),
          'edadBeneficiario': forms.TextInput(attrs={'class': 'form-control'}),
          'parenscoBeneficiario': forms.Select(attrs={'class': 'form-control'}),
          'porcentajeBeneficiario': forms.TextInput(attrs={'class': 'form-control'})
        }

class refereciasForm(forms.ModelForm):
    class Meta:
        model = referencias
        fields = ['nombreReferencia', 'telReferencia', 'correoReferencia', 'tipoReferencia']
        labels = {
            'nombreReferencia': 'Nombre:',
            'telReferencia': 'Telefono:',
            'correoReferencia': 'Correo Referencia:',
            'tipoReferencia': 'Tipo de Referenca:',
        }
        widgets = {
          'nombreReferencia': forms.TextInput(attrs={'class': 'form-control'}),
          'telReferencia': forms.TextInput(attrs={'class': 'form-control'}),
          'correoReferencia': forms.TextInput(attrs={'class': 'form-control'}),
          'tipoReferencia': forms.Select(attrs={'class': 'form-control'}),
        }

class trabajosForm(forms.ModelForm):
    class Meta:
        model = trabajo
        fields = ['capacidadPago', 'catalogoProfesiones_idcatalogoProfesiones', 'tipoActEconomica_idTipoActEconomica']
        labels = {
            'capacidadPago': 'Capacidad de pago:',
            'catalogoProfesiones_idcatalogoProfesiones': 'Profesion:',
            'tipoActEconomica_idTipoActEconomica': 'Actividad economica:',
        }
        widgets = {
          'capacidadPago': forms.TextInput(attrs={'class': 'form-control'}),
          'catalogoProfesiones_idcatalogoProfesiones': forms.Select(attrs={'class': 'form-control'}),
          'tipoActEconomica_idTipoActEconomica': forms.Select(attrs={'class': 'form-control'}),
        }

class documentosForm(forms.ModelForm):
    class Meta:
        model = catalogoDocumentos
        fields = ['numDocumento', 'tipoDocumento_idTipoDocumento']
        labels = {
            'numDocumento': 'Numero de documento:',
            'tipoDocumento_idTipoDocumento': 'Tipo de documento:',
        }
        widgets = {
          'numDocumento': forms.TextInput(attrs={'class': 'form-control'}),
          'tipoDocumento_idTipoDocumento': forms.Select(attrs={'class': 'form-control'}),
        }

class asociacionForm(forms.ModelForm):
    class Meta:
        model = asociacion
        fields = ['fechaAsociacion', 'lugarAsociacion', 'estadoAsociacion', 'ejecutivo_idEjecutivo']
        labels = {
            'fechaAsociacion': 'Fecha de solicitud:',
            'lugarAsociacion': 'Lugar de solicitud:',
            'estadoAsociacion': 'Estado del asociado:',
            'ejecutivo_idEjecutivo': 'Ejecutivo:',
        }
        widgets = {
          'fechaAsociacion': forms.TextInput(attrs={'class': 'form-control'}),
          'lugarAsociacion': forms.TextInput(attrs={'class': 'form-control'}),
          'estadoAsociacion': forms.Select(attrs={'class': 'form-control'}),
          'ejecutivo_idEjecutivo': forms.Select(attrs={'class': 'form-control'}),
        }