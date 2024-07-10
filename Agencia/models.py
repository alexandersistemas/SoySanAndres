from django.db import models
from django.urls import reverse


def __str__(self):
    return str(self.Nombre)

class Ciudad(models.Model):

    # Relationships
    idPais = models.ForeignKey("Agencia.Pais", on_delete=models.CASCADE)

    # Fields
    idCiudad = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_Ciudad_detail", args=(self.idCiudad,))

    def get_update_url(self):
        return reverse("Agencia_Ciudad_update", args=(self.idCiudad,))



class TipoDocumento(models.Model):
    # Fields
    idTipoDocumento = models.AutoField(primary_key=True)
    Nombre          = models.CharField(max_length=45)

    class Meta:
        pass

    def __str__(self):
        return str(self.Nombre)

    # def get_absolute_url(self):
    #     return reverse("Agencia_TipoDocumento_detail", args=(self.idTipoDocumento,))
    #
    # def get_update_url(self):
    #     return reverse("Agencia_TipoDocumento_update", args=(self.idTipoDocumento,))



class Cliente(models.Model):

    # Relationships
    idCiudad = models.ForeignKey("Agencia.Ciudad", on_delete=models.CASCADE)
    idTipoDocumento = models.ForeignKey("Agencia.TipoDocumento", on_delete=models.CASCADE)

    # Fields
    idCliente = models.AutoField(primary_key=True)
    NumeroDocumento = models.IntegerField()
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    FechaNacimiento = models.DateField()
    Direccion = models.CharField(max_length=45, null=True)
    Telefono2 = models.CharField(max_length=45)
    Telefono1 = models.CharField(max_length=45, null=True)
    Correo = models.EmailField()
    Password = models.CharField(max_length=45, default='nopws')
    FechaCreado = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.Nombres)


class Promotor(models.Model):

    # Relationships
    idTipoDocumento = models.ForeignKey("Agencia.TipoDocumento", on_delete=models.CASCADE)

    # Fields
    idPromotor = models.AutoField(primary_key=True)
    NumeroDocumento = models.IntegerField()
    Nombres = models.CharField(max_length=45)
    Apellidos = models.CharField(max_length=45)
    PorcentajeComision = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_Promotor_detail", args=(self.idPromotor,))

    def get_update_url(self):
        return reverse("Agencia_Promotor_update", args=(self.idPromotor,))


class PlanImagen(models.Model):

    # Relationships
    idPlan = models.ForeignKey("Agencia.PlanTuristico", on_delete=models.CASCADE)
    idImagen = models.ForeignKey("Agencia.Imagen", on_delete=models.CASCADE)

    # Fields
    idPlanImagen = models.AutoField(primary_key=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_PlanImagen_detail", args=(self.idPlanImagen,))

    def get_update_url(self):
        return reverse("Agencia_PlanImagen_update", args=(self.idPlanImagen,))


class Estado(models.Model):

    # Fields
    idEstado = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=45)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_Estado_detail", args=(self.idEstado,))

    def get_update_url(self):
        return reverse("Agencia_Estado_update", args=(self.idEstado,))


class TransaccionPlan(models.Model):

    # Relationships
    idTransaccion = models.ForeignKey("Agencia.Transaccion", on_delete=models.CASCADE)
    idPlan = models.ForeignKey("Agencia.PlanTuristico", on_delete=models.CASCADE)

    # Fields
    idTransaccionPlan = models.AutoField(primary_key=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_TransaccionPlan_detail", args=(self.idTransaccionPlan,))

    def get_update_url(self):
        return reverse("Agencia_TransaccionPlan_update", args=(self.idTransaccionPlan,))


class TipoParentesco(models.Model):

    # Fields
    idTipoParentesco = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=45)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    # def get_absolute_url(self):
    #     return reverse("Agencia_TipoParentesco_detail", args=(self.idTipoParentesco,))
    #
    # def get_update_url(self):
    #     return reverse("Agencia_TipoParentesco_update", args=(self.idTipoParentesco,))




class Promocion(models.Model):

    # Fields
    idPromocion = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=45)
    Descripcion = models.TextField(max_length=255)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()
    PrecioPeso = models.IntegerField()
    PrecioDolar = models.IntegerField()
    FechaCreado = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_Promocion_detail", args=(self.idPromocion,))

    def get_update_url(self):
        return reverse("Agencia_Promocion_update", args=(self.idPromocion,))


class TipoPQRS(models.Model):

    # Fields
    idTipoPQRS = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_TipoPQRS_detail", args=(self.idTipoPQRS,))

    def get_update_url(self):
        return reverse("Agencia_TipoPQRS_update", args=(self.idTipoPQRS,))


class Integrante(models.Model):

    # Relationships
    idCliente = models.ForeignKey("Agencia.Cliente", on_delete=models.CASCADE)
    idTipoParentesco = models.ForeignKey("Agencia.TipoParentesco", on_delete=models.CASCADE, null=True)
    idTipoDocumento = models.ForeignKey("Agencia.TipoDocumento", on_delete=models.CASCADE)

    # Fields
    idIntegrante = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=45)
    Apellidos = models.CharField(max_length=45)
    NumeroDocumento = models.IntegerField()
    FechaCreado = models.DateTimeField(auto_now_add=True, editable=False)
    FechaNacimiento = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.Nombres)


class Transaccion(models.Model):

    # Relationships
    idCupon = models.ForeignKey("Agencia.Cupon", on_delete=models.CASCADE, null=True)
    idEstado = models.ForeignKey("Agencia.Estado", on_delete=models.CASCADE)
    idCliente = models.ForeignKey("Agencia.Cliente", on_delete=models.CASCADE)
    idPromotor = models.ForeignKey("Agencia.Promotor", on_delete=models.CASCADE, null=True)

    # Fields
    idTransaccion = models.AutoField(primary_key=True)
    FechaCreado = models.DateTimeField(auto_now_add=True, editable=False)
    Valor = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.FechaCreado)



class PQRS(models.Model):

    # Relationships
    idTipoPQRS = models.ForeignKey("Agencia.TipoPQRS", on_delete=models.CASCADE)
    idCliente = models.ForeignKey("Agencia.Cliente", on_delete=models.CASCADE)

    # Fields
    idPQRS = models.AutoField(primary_key=True)
    FechaCreado = models.DateTimeField(auto_now_add=True, editable=False)
    Descripcion = models.TextField(max_length=255)

    class Meta:
        pass

    def __str__(self):
        return str(self.Descripcion)

class TransaccionPromocion(models.Model):

    # Relationships
    idPromocion = models.ForeignKey("Agencia.Promocion", on_delete=models.CASCADE)
    idTransaccion = models.ForeignKey("Agencia.Transaccion", on_delete=models.CASCADE)

    # Fields
    idTransaccionPromocion = models.AutoField(primary_key=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_TransaccionPromocion_detail", args=(self.idTransaccionPromocion,))

    def get_update_url(self):
        return reverse("Agencia_TransaccionPromocion_update", args=(self.idTransaccionPromocion,))


class Pais(models.Model):

    # Fields
    idPais = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=45)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_Pais_detail", args=(self.idPais,))

    def get_update_url(self):
        return reverse("Agencia_Pais_update", args=(self.idPais,))


class Cupon(models.Model):

    # Fields
    idCupon = models.AutoField(primary_key=True)
    FechaCreado = models.DateTimeField(auto_now_add=True, editable=False)
    Porcentaje = models.IntegerField()
    Cupon = models.CharField(max_length=45)
    FechaInicio = models.DateField()
    FechaFin = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_Cupon_detail", args=(self.idCupon,))

    def get_update_url(self):
        return reverse("Agencia_Cupon_update", args=(self.idCupon,))


class Imagen(models.Model):

    # Fields
    idImagen = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=45)
    FechaCreado = models.DateTimeField(auto_now_add=True, editable=False)
    Ruta = models.CharField(max_length=45)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_Imagen_detail", args=(self.idImagen,))

    def get_update_url(self):
        return reverse("Agencia_Imagen_update", args=(self.idImagen,))


class PromocionImagen(models.Model):

    # Relationships
    idImagen = models.ForeignKey("Agencia.Imagen", on_delete=models.CASCADE)
    idPromocion = models.ForeignKey("Agencia.Promocion", on_delete=models.CASCADE)

    # Fields
    idPromocionImagen = models.AutoField(primary_key=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Agencia_PromocionImagen_detail", args=(self.idPromocionImagen,))

    def get_update_url(self):
        return reverse("Agencia_PromocionImagen_update", args=(self.idPromocionImagen,))


class PlanTuristico(models.Model):

    # Fields
    idPlan = models.AutoField(primary_key=True)
    Descripcion = models.TextField(max_length=255)
    Capacidad = models.IntegerField(null=True)
    Nombre = models.CharField(max_length=100)
    PrecioDolar = models.IntegerField()
    PrecioPeso = models.IntegerField()

    class Meta:
        pass





