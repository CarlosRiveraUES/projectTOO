from dataclasses import asdict
from django.db import models


# Create your models here.

class genero(models.Model):
    idGenero = models.AutoField(primary_key=True)
    # Por sno funciona lo de abajo esta la linea 36
    # nombreGenero = models.CharField(max_length=8, unique=True)
    nombreGenero = models.CharField(max_length=10)
        
    class Meta:
        managed = True
        db_table = 'genero'
    def __str__(self):
        return f'{self.nombreGenero}'


class cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    primerNombre = models.CharField(max_length=45)
    segundoNombre = models.CharField(max_length=45)
    primerApellido = models.CharField(max_length=45)
    segundoApellido= models.CharField(max_length=45)
    apellidoCasada = models.CharField(max_length=45, blank=True, null=True)
    fechaNacimiento = models.CharField(max_length=11)
    nacionalidad = models.CharField(max_length=45)
    paisNacimiento = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=100)
    subRegion = models.CharField(max_length=50)
    ESTADOCIVIL= (
        ('1', 'CASADO'),
        ('2', 'DIVORCIADO'),
        ('3','VIUDO'),
        ('4','SOLTERO'),
    )
    estadoCivil = models.CharField(max_length=2, choices=ESTADOCIVIL)
    genero_idGenero = models.ForeignKey(genero, on_delete=models.CASCADE)    
    class Meta:
        managed = True
        db_table = 'cliente'
    def __str__(self):
        return f'{self. idCliente}'


# Tabla ejecutico
class ejecutivo(models.Model):
    idEjecutivo = models.AutoField(primary_key=True)
    nombreEjecutivo = models.CharField(max_length=50)
    apellidoEjecutivo = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'ejecutivo'
    def __str__(self):
        return f'{self.nombreEjecutivo}'

# Create your models here.
class asociacion(models.Model):
    idAsociado = models.AutoField(primary_key=True)
    fechaAsociacion = models.CharField(max_length=50)
    lugarAsociacion = models.CharField(max_length=100)
    ESTADO= (
        ('1', 'Espera de pago'),
        ('2', 'Verificacion de solicitud'),
        ('3', 'Aprobado'),
        ('4', 'Rechazado'),
    )
    estadoAsociacion = models.CharField(max_length=100, choices=ESTADO, null=True)
    cliente_idCliente = models.ForeignKey(cliente, null=True, on_delete= models.CASCADE)
    ejecutivo_idEjecutivo= models.ForeignKey(ejecutivo, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'asociacion'
    def __str__(self):
        return f'{self.idAsociado}'

# Tabla tipo documento
class tipoDocumento(models.Model):
    idTipoDocumento = models.AutoField(primary_key=True)
    # Por sno funciona lo de abajo esta la linea 52
    # nombreDocumento = models.CharField(max_length=10, unique=True)
    nombreDocumento = models.CharField(max_length=50)
        
    class Meta:
        managed = True
        db_table = 'tipoDocumento'
    def __str__(self):
        return f'{self.nombreDocumento}'

#Tabla actividad economica
class tipoActEconomica(models.Model):
    idTipoActEconomica = models.AutoField(primary_key=True)
    nombreActEconomica= models.CharField(max_length=50)
    rubroActEconomica= models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'tipoActEconomica'
    def __str__(self):
        return f'{self.nombreActEconomica}'

#Tabla Catalogo de profeciones
class catalogoProfesiones(models.Model):
    idCatalogoProfesiones = models.AutoField(primary_key=True)
    nombreProfesion= models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'catalogoProfesiones'
    def __str__(self):
        return f'{self.nombreProfesion}'

#Tabla beneficiario

class beneficiario(models.Model):
    idBeneficiario = models.AutoField(primary_key=True)
    nombreBeneficiario= models.CharField(max_length=50)
    apellidoBeneficiario= models.CharField(max_length=50)
    telBeneficiario= models.CharField(max_length=20)
    edadBeneficiario = models.IntegerField()
    PARENTESCO = (
        ('1', 'MAMÁ'),
        ('2', 'PAPÁ'),
        ('3','HERMANO/A'),
        ('4','ABUELA/O'),
        ('5','HIJO/A'),
        ('6','TIO/A'),
        ('7','NIETO/A'),
        ('8','SOBRINO'),
        ('9','PRIMA/O'),
    )
    parenscoBeneficiario = models.CharField(max_length=2, choices=PARENTESCO)
    porcentajeBeneficiario = models.CharField(max_length=20, null=True)
    clienteBeneficiario = models.ForeignKey(cliente, null=True, on_delete=models.CASCADE)
    class Meta:
        managed = True
        db_table = 'beneficiario'
    def __str__(self):
        return f'{self.idBeneficiario}'

#Catalogo actividad economica
class trabajo(models.Model):
    idTrabajo = models.AutoField(primary_key=True)
    capacidadPago = models.CharField(max_length=150)
    cliente_idCliente = models.ForeignKey(cliente, null=True, on_delete=models.CASCADE)
    catalogoProfesiones_idcatalogoProfesiones = models.ForeignKey(catalogoProfesiones, on_delete=models.CASCADE)
    tipoActEconomica_idTipoActEconomica = models.ForeignKey(tipoActEconomica, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'trabajo'
    def __str__(self):
        return f'{self.idTrabajo}'
#Catalogo documentos
class catalogoDocumentos(models.Model):
    idCatalogoDocumentos = models.AutoField(primary_key=True)
    numDocumento = models.CharField(max_length=50)
    cliente_idCliente = models.ForeignKey(cliente, null=True, on_delete=models.CASCADE)
    tipoDocumento_idTipoDocumento = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'catalogoDocumentos'
    def __str__(self):
        return f'{self.idCatalogoDocumentos}'

#Tabla referencias
class referencias(models.Model):
    idReferenciaCliente = models.AutoField(primary_key=True)
    nombreReferencia = models.CharField(max_length=100)
    telReferencia = models.CharField(max_length=20)
    correoReferencia = models.CharField(max_length=100)
    TIPOREFERENCIA = (
        ('1', 'PERSONAL'),
        ('2', 'FAMILIAR'),
    )
    tipoReferencia = models.CharField(max_length=2, null=True, choices=TIPOREFERENCIA)
    cliente_idCliente3 = models.ForeignKey(cliente, null=True, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'referencias'
    def __str__(self):
        return f'{self.idReferenciaCliente}'

#recibo
class recibo(models.Model):
    idRecibo = models.AutoField(primary_key=True)
    fechaPago = models.CharField(max_length=100)
    montoPago = models.FloatField()
    asociacio_idRecibo = models.ForeignKey(asociacion, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'recibo'
    def __str__(self):
        return f'{self.idRecibo}'

class usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=50)
    usuarioCliente = models.ForeignKey(cliente, on_delete=models.CASCADE)    

    class Meta:
        managed = True
        db_table = 'usuario'
    def _str_(self):
        return f'{self.idUsuario}'

class cuentaAportaciones(models.Model):
    idcuentaAportaciones = models.AutoField(primary_key=True)
    cuotaMensual = models.FloatField()
    fechaAportacion = models.CharField(max_length=50)
    aportacionesAsociacion = models.ForeignKey(asociacion, on_delete=models.CASCADE)    

    class Meta:
        managed = True
        db_table = 'cuentaAportaciones'
    def _str_(self):
        return f'{self.idcuentaAportaciones}'

class cuentaAhorros(models.Model):
    idCuentaAhorros = models.AutoField(primary_key=True)
    numCuentaAhorros = models.IntegerField()
    saldoActual = models.FloatField()
    movimientoAbonoRetiro = models.FloatField()
    saldoAnterior = models.FloatField()
    ahorrosAsociacion = models.ForeignKey(asociacion, on_delete=models.CASCADE)    

    class Meta:
        managed = True
        db_table = 'cuentaAhorros'
    def _str_(self):
        return f'{self.idCuentaAhorros}'

class actaAsociado (models.Model):
    idActaAsociado = models.AutoField(primary_key=True)
    firmaPresidente = models.CharField(max_length=100)
    firmaSecretaria= models.CharField(max_length=100)
    numActa = models.IntegerField()
    fechaActa = models.DateField() 

    class Meta:
        managed = True
        db_table = 'actaAsociado'
    def _str_(self):
        return f'{self.idActaAsociado}'
        