from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PromotorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Promotor class"""

    queryset = models.Promotor.objects.all()
    serializer_class = serializers.PromotorSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlanImagenViewSet(viewsets.ModelViewSet):
    """ViewSet for the PlanImagen class"""

    queryset = models.PlanImagen.objects.all()
    serializer_class = serializers.PlanImagenSerializer
    permission_classes = [permissions.IsAuthenticated]


class EstadoViewSet(viewsets.ModelViewSet):
    """ViewSet for the Estado class"""

    queryset = models.Estado.objects.all()
    serializer_class = serializers.EstadoSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransaccionPlanViewSet(viewsets.ModelViewSet):
    """ViewSet for the TransaccionPlan class"""

    queryset = models.TransaccionPlan.objects.all()
    serializer_class = serializers.TransaccionPlanSerializer
    permission_classes = [permissions.IsAuthenticated]


# class TipoParentescoViewSet(viewsets.ModelViewSet):
#     """ViewSet for the TipoParentesco class"""
#
#     queryset = models.TipoParentesco.objects.all()
#     serializer_class = serializers.TipoParentescoSerializer
#     permission_classes = [permissions.IsAuthenticated]


class TipoDocumentoViewSet(viewsets.ModelViewSet):
    """ViewSet for the TipoDocumento class"""

    queryset = models.TipoDocumento.objects.all()
    serializer_class = serializers.TipoDocumentoSerializer
    permission_classes = [permissions.IsAuthenticated]


class PromocionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Promocion class"""

    queryset = models.Promocion.objects.all()
    serializer_class = serializers.PromocionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TipoPQRSViewSet(viewsets.ModelViewSet):
    """ViewSet for the TipoPQRS class"""

    queryset = models.TipoPQRS.objects.all()
    serializer_class = serializers.TipoPQRSSerializer
    permission_classes = [permissions.IsAuthenticated]


class IntegranteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Integrante class"""

    queryset = models.Integrante.objects.all()
    serializer_class = serializers.IntegranteSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransaccionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Transaccion class"""

    queryset = models.Transaccion.objects.all()
    serializer_class = serializers.TransaccionSerializer
    permission_classes = [permissions.IsAuthenticated]


class CiudadViewSet(viewsets.ModelViewSet):
    """ViewSet for the Ciudad class"""

    queryset = models.Ciudad.objects.all()
    serializer_class = serializers.CiudadSerializer
    permission_classes = [permissions.IsAuthenticated]


class PQRSViewSet(viewsets.ModelViewSet):
    """ViewSet for the PQRS class"""

    queryset = models.PQRS.objects.all()
    serializer_class = serializers.PQRSSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransaccionPromocionViewSet(viewsets.ModelViewSet):
    """ViewSet for the TransaccionPromocion class"""

    queryset = models.TransaccionPromocion.objects.all()
    serializer_class = serializers.TransaccionPromocionSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaisViewSet(viewsets.ModelViewSet):
    """ViewSet for the Pais class"""

    queryset = models.Pais.objects.all()
    serializer_class = serializers.PaisSerializer
    permission_classes = [permissions.IsAuthenticated]


class CuponViewSet(viewsets.ModelViewSet):
    """ViewSet for the Cupon class"""

    queryset = models.Cupon.objects.all()
    serializer_class = serializers.CuponSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImagenViewSet(viewsets.ModelViewSet):
    """ViewSet for the Imagen class"""

    queryset = models.Imagen.objects.all()
    serializer_class = serializers.ImagenSerializer
    permission_classes = [permissions.IsAuthenticated]


class PromocionImagenViewSet(viewsets.ModelViewSet):
    """ViewSet for the PromocionImagen class"""

    queryset = models.PromocionImagen.objects.all()
    serializer_class = serializers.PromocionImagenSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlanTuristicoViewSet(viewsets.ModelViewSet):
    """ViewSet for the PlanTuristico class"""

    queryset = models.PlanTuristico.objects.all()
    serializer_class = serializers.PlanTuristicoSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClienteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Cliente class"""

    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
