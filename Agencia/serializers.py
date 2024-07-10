from rest_framework import serializers

from . import models


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cliente
        fields = [
            "Telefono2",
            "FechaCreado",
            "Direccion",
            "Telefono1",
            "FechaNacimiento",
            "NumeroDocumento",
            "Correo",
            "Apellidos",
            "Nombres",
        ]

class PromotorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Promotor
        fields = [
            "Nombres",
            "PorcentajeComision",
            "idPromotor",
            "NumeroDocumento",
            "Apellidos",
        ]

class PlanImagenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanImagen
        fields = [
            "idPlanImagen",
        ]

class EstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Estado
        fields = [
            "idEstado",
            "Nombre",
        ]

class TransaccionPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TransaccionPlan
        fields = [
            "idTransaccionPlan",
        ]

class TipoParentescoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TipoParentesco
        fields = [
            "idTipoParentesco",
            "Nombre",
        ]

class TipoDocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TipoDocumento
        fields = [
            "Nombre",
            "idTipoDocumento",
        ]

class PromocionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Promocion
        fields = [
            "FechaInicio",
            "idPromocion",
            "Nombre",
            "PrecioPeso",
            "Descripcion",
            "FechaFin",
            "PrecioDolar",
            "FechaCreado",
        ]

class TipoPQRSSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TipoPQRS
        fields = [
            "Nombre",
            "idTipoPQRS",
        ]

class IntegranteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Integrante
        fields = [
            "Apellidos",
            "idIntegrante",
            "FechaCreado",
            "Nombres",
            "NumeroDocumento",
            "FechaNacimiento",
        ]

class TransaccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transaccion
        fields = [
            "FechaCreado",
            "idTransaccion",
            "Valor",
        ]

class CiudadSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ciudad
        fields = [
            "Nombre",
            "idCiudad",
        ]

class PQRSSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PQRS
        fields = [
            "FechaCreado",
            "Descripcion",
        ]

class TransaccionPromocionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TransaccionPromocion
        fields = [
            "idTransaccionPromocion",
        ]

class PaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pais
        fields = [
            "idPais",
            "Nombre",
        ]

class CuponSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cupon
        fields = [
            "FechaCreado",
            "Porcentaje",
            "idCupon",
            "Cupon",
            "FechaInicio",
            "FechaFin",
        ]

class ImagenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Imagen
        fields = [
            "FechaCreado",
            "Ruta",
            "Nombre",
            "idImagen",
        ]

class PromocionImagenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PromocionImagen
        fields = [
            "idPromocionImagen",
        ]

class PlanTuristicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PlanTuristico
        fields = [
            "idPlan",
            "Descripcion",
            "Capacidad",
            "Nombre",
            "PrecioDolar",
            "PrecioPeso",
        ]


