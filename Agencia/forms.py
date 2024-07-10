from . import models
from django import forms


class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = [
            "NumeroDocumento",
            "Nombres",
            "Apellidos",
            "FechaNacimiento",
            "Direccion",
            "Telefono1",
            "Telefono2",
            "Correo",
            "Password",
        ]

class CiudadForm(forms.ModelForm):
    class Meta:
        model = models.Ciudad
        fields = [
            "Nombre",
            "idPais",
        ]


class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = models.TipoDocumento
        fields = [
            "Nombre",
        ]

class PromotorForm(forms.ModelForm):
    class Meta:
        model = models.Promotor
        fields = [
            "Nombres",
            "PorcentajeComision",
            "NumeroDocumento",
            "Apellidos",
            "idTipoDocumento",
        ]


class PlanImagenForm(forms.ModelForm):
    class Meta:
        model = models.PlanImagen
        fields = [
            "idPlan",
            "idImagen",
        ]


class EstadoForm(forms.ModelForm):
    class Meta:
        model = models.Estado
        fields = [
            "Nombre",
        ]


class TransaccionPlanForm(forms.ModelForm):
    class Meta:
        model = models.TransaccionPlan
        fields = [
            "idTransaccion",
            "idPlan",
        ]


class PromocionForm(forms.ModelForm):
    class Meta:
        model = models.Promocion
        fields = [
            "FechaInicio",
            "Nombre",
            "PrecioPeso",
            "Descripcion",
            "FechaFin",
            "PrecioDolar",
        ]


class TipoPQRSForm(forms.ModelForm):
    class Meta:
        model = models.TipoPQRS
        fields = [
            "Nombre",
        ]



class TransaccionPromocionForm(forms.ModelForm):
    class Meta:
        model = models.TransaccionPromocion
        fields = [
            "idPromocion",
            "idTransaccion",
        ]


class PaisForm(forms.ModelForm):
    class Meta:
        model = models.Pais
        fields = [
            "Nombre",
        ]


class CuponForm(forms.ModelForm):
    class Meta:
        model = models.Cupon
        fields = [
            "Porcentaje",
            "Cupon",
            "FechaInicio",
            "FechaFin",
        ]


class ImagenForm(forms.ModelForm):
    class Meta:
        model = models.Imagen
        fields = [
            "Ruta",
            "Nombre",
        ]


class PromocionImagenForm(forms.ModelForm):
    class Meta:
        model = models.PromocionImagen
        fields = [
            "idImagen",
            "idPromocion",
        ]


class PlanTuristicoForm(forms.ModelForm):
    class Meta:
        model = models.PlanTuristico
        fields = [
            "Descripcion",
            "Capacidad",
            "Nombre",
            "PrecioDolar",
            "PrecioPeso",
        ]



