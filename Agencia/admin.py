from django.contrib import admin
from django import forms

from . import models

class ClienteAdminForm(forms.ModelForm):

    class Meta:
        model = models.Cliente
        fields = "__all__"

class ClienteAdmin(admin.ModelAdmin):
    form = ClienteAdminForm
    list_display = [
        "Telefono2",
        "FechaCreado",
        "Direccion",
        "Telefono1",
        "FechaNacimiento",
        "NumeroDocumento",
        "Correo",
        "Apellidos",
        "Nombres",
        "idCliente",
    ]
    readonly_fields = [
        "Telefono2",
        "FechaCreado",
        "Direccion",
        "Telefono1",
        "FechaNacimiento",
        "NumeroDocumento",
        "Correo",
        "Apellidos",
        "Nombres",
        "idCliente",
    ]

class PromotorAdminForm(forms.ModelForm):

    class Meta:
        model = models.Promotor
        fields = "__all__"


class PromotorAdmin(admin.ModelAdmin):
    form = PromotorAdminForm
    list_display = [
        "Nombres",
        "PorcentajeComision",
        "idPromotor",
        "NumeroDocumento",
        "Apellidos",
    ]
    readonly_fields = [
        "Nombres",
        "PorcentajeComision",
        "idPromotor",
        "NumeroDocumento",
        "Apellidos",
    ]


class PlanImagenAdminForm(forms.ModelForm):

    class Meta:
        model = models.PlanImagen
        fields = "__all__"


class PlanImagenAdmin(admin.ModelAdmin):
    form = PlanImagenAdminForm
    list_display = [
        "idPlanImagen",
    ]
    readonly_fields = [
        "idPlanImagen",
    ]


class EstadoAdminForm(forms.ModelForm):

    class Meta:
        model = models.Estado
        fields = "__all__"


class EstadoAdmin(admin.ModelAdmin):
    form = EstadoAdminForm
    list_display = [
        "idEstado",
        "Nombre",
    ]
    readonly_fields = [
        "idEstado",
        "Nombre",
    ]


class TransaccionPlanAdminForm(forms.ModelForm):

    class Meta:
        model = models.TransaccionPlan
        fields = "__all__"


class TransaccionPlanAdmin(admin.ModelAdmin):
    form = TransaccionPlanAdminForm
    list_display = [
        "idTransaccionPlan",
    ]
    readonly_fields = [
        "idTransaccionPlan",
    ]


# class TipoParentescoAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = models.TipoParentesco
#         fields = "__all__"
#
#
# class TipoParentescoAdmin(admin.ModelAdmin):
#     form = TipoParentescoAdminForm
#     list_display = [
#         "idTipoParentesco",
#         "Nombre",
#     ]
#     readonly_fields = [
#         "idTipoParentesco",
#         "Nombre",
#     ]


class TipoDocumentoAdminForm(forms.ModelForm):

    class Meta:
        model = models.TipoDocumento
        fields = "__all__"


class TipoDocumentoAdmin(admin.ModelAdmin):
    form = TipoDocumentoAdminForm
    list_display = [
        "Nombre",
        "idTipoDocumento",
    ]
    readonly_fields = [
        "Nombre",
        "idTipoDocumento",
    ]


class PromocionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Promocion
        fields = "__all__"


class PromocionAdmin(admin.ModelAdmin):
    form = PromocionAdminForm
    list_display = [
        "FechaInicio",
        "idPromocion",
        "Nombre",
        "PrecioPeso",
        "Descripcion",
        "FechaFin",
        "PrecioDolar",
        "FechaCreado",
    ]
    readonly_fields = [
        "FechaInicio",
        "idPromocion",
        "Nombre",
        "PrecioPeso",
        "Descripcion",
        "FechaFin",
        "PrecioDolar",
        "FechaCreado",
    ]


class TipoPQRSAdminForm(forms.ModelForm):

    class Meta:
        model = models.TipoPQRS
        fields = "__all__"


class TipoPQRSAdmin(admin.ModelAdmin):
    form = TipoPQRSAdminForm
    list_display = [
        "Nombre",
        "idTipoPQRS",
    ]
    readonly_fields = [
        "Nombre",
        "idTipoPQRS",
    ]


# class IntegranteAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = models.Integrante
#         fields = "__all__"


# class IntegranteAdmin(admin.ModelAdmin):
#     form = IntegranteAdminForm
#     list_display = [
#         "Apellidos",
#         "idIntegrante",
#         "FechaCreado",
#         "Nombres",
#         "FechaNacimiento",
#     ]
#     readonly_fields = [
#         "Apellidos",
#         "idIntegrante",
#         "FechaCreado",
#         "Nombres",
#         "FechaNacimiento",
#     ]


class TransaccionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Transaccion
        fields = "__all__"


class TransaccionAdmin(admin.ModelAdmin):
    form = TransaccionAdminForm
    list_display = [
        "FechaCreado",
        "idTransaccion",
        "Valor",
    ]
    readonly_fields = [
        "FechaCreado",
        "idTransaccion",
        "Valor",
    ]


class CiudadAdminForm(forms.ModelForm):

    class Meta:
        model = models.Ciudad
        fields = "__all__"


class CiudadAdmin(admin.ModelAdmin):
    form = CiudadAdminForm
    list_display = [
        "Nombre",
        "idCiudad",
    ]
    readonly_fields = [
        "Nombre",
        "idCiudad",
    ]


class PQRSAdminForm(forms.ModelForm):

    class Meta:
        model = models.PQRS
        fields = "__all__"


class PQRSAdmin(admin.ModelAdmin):
    form = PQRSAdminForm
    list_display = [
        "FechaCreado",
        "Descripcion",
    ]
    readonly_fields = [
        "FechaCreado",
        "Descripcion",
    ]


class TransaccionPromocionAdminForm(forms.ModelForm):

    class Meta:
        model = models.TransaccionPromocion
        fields = "__all__"


class TransaccionPromocionAdmin(admin.ModelAdmin):
    form = TransaccionPromocionAdminForm
    list_display = [
        "idTransaccionPromocion",
    ]
    readonly_fields = [
        "idTransaccionPromocion",
    ]


class PaisAdminForm(forms.ModelForm):

    class Meta:
        model = models.Pais
        fields = "__all__"


class PaisAdmin(admin.ModelAdmin):
    form = PaisAdminForm
    list_display = [
        "idPais",
        "Nombre",
    ]
    readonly_fields = [
        "idPais",
        "Nombre",
    ]


class CuponAdminForm(forms.ModelForm):

    class Meta:
        model = models.Cupon
        fields = "__all__"


class CuponAdmin(admin.ModelAdmin):
    form = CuponAdminForm
    list_display = [
        "FechaCreado",
        "Porcentaje",
        "idCupon",
        "Cupon",
        "FechaInicio",
        "FechaFin",
    ]
    readonly_fields = [
        "FechaCreado",
        "Porcentaje",
        "idCupon",
        "Cupon",
        "FechaInicio",
        "FechaFin",
    ]


class ImagenAdminForm(forms.ModelForm):

    class Meta:
        model = models.Imagen
        fields = "__all__"


class ImagenAdmin(admin.ModelAdmin):
    form = ImagenAdminForm
    list_display = [
        "FechaCreado",
        "Ruta",
        "Nombre",
        "idImagen",
    ]
    readonly_fields = [
        "FechaCreado",
        "Ruta",
        "Nombre",
        "idImagen",
    ]


class PromocionImagenAdminForm(forms.ModelForm):

    class Meta:
        model = models.PromocionImagen
        fields = "__all__"


class PromocionImagenAdmin(admin.ModelAdmin):
    form = PromocionImagenAdminForm
    list_display = [
        "idPromocionImagen",
    ]
    readonly_fields = [
        "idPromocionImagen",
    ]


class PlanTuristicoAdminForm(forms.ModelForm):

    class Meta:
        model = models.PlanTuristico
        fields = "__all__"


class PlanTuristicoAdmin(admin.ModelAdmin):
    form = PlanTuristicoAdminForm
    list_display = [
        "idPlan",
        "Descripcion",
        "Capacidad",
        "Nombre",
        "PrecioDolar",
        "PrecioPeso",
    ]
    readonly_fields = [
        "idPlan",
        "Descripcion",
        "Capacidad",
        "Nombre",
        "PrecioDolar",
        "PrecioPeso",
    ]








admin.site.register(models.Promotor, PromotorAdmin)
admin.site.register(models.PlanImagen, PlanImagenAdmin)
admin.site.register(models.Estado, EstadoAdmin)
admin.site.register(models.TransaccionPlan, TransaccionPlanAdmin)
# admin.site.register(models.TipoParentesco, TipoParentescoAdmin)
admin.site.register(models.TipoDocumento, TipoDocumentoAdmin)
admin.site.register(models.Promocion, PromocionAdmin)
admin.site.register(models.TipoPQRS, TipoPQRSAdmin)
# admin.site.register(models.Integrante, IntegranteAdmin)
admin.site.register(models.Transaccion, TransaccionAdmin)
admin.site.register(models.Ciudad, CiudadAdmin)
admin.site.register(models.PQRS, PQRSAdmin)
admin.site.register(models.TransaccionPromocion, TransaccionPromocionAdmin)
admin.site.register(models.Pais, PaisAdmin)
admin.site.register(models.Cupon, CuponAdmin)
admin.site.register(models.Imagen, ImagenAdmin)
admin.site.register(models.PromocionImagen, PromocionImagenAdmin)
admin.site.register(models.PlanTuristico, PlanTuristicoAdmin)
admin.site.register(models.Cliente, ClienteAdmin)
