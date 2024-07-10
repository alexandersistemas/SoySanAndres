from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register("Promotor", api.PromotorViewSet)
router.register("PlanImagen", api.PlanImagenViewSet)
router.register("Estado", api.EstadoViewSet)
router.register("TransaccionPlan", api.TransaccionPlanViewSet)
# router.register("TipoParentesco", api.TipoParentescoViewSet)
router.register("TipoDocumento", api.TipoDocumentoViewSet)
router.register("Promocion", api.PromocionViewSet)
router.register("TipoPQRS", api.TipoPQRSViewSet)
# router.register("Integrante", api.IntegranteViewSet)
router.register("Transaccion", api.TransaccionViewSet)
router.register("Ciudad", api.CiudadViewSet)
router.register("PQRS", api.PQRSViewSet)
router.register("TransaccionPromocion", api.TransaccionPromocionViewSet)
router.register("Pais", api.PaisViewSet)
router.register("Cupon", api.CuponViewSet)
router.register("Imagen", api.ImagenViewSet)
router.register("PromocionImagen", api.PromocionImagenViewSet)
router.register("PlanTuristico", api.PlanTuristicoViewSet)
router.register("Cliente", api.ClienteViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Agencia/Registro/", views.formularioRegistro, name="registroform"),
    path('Agencia/Ponton/', TemplateView.as_view(template_name='PlanPonton.html'), name='pontonform'),
    path("Agencia/Promotor/", views.PromotorListView.as_view(), name="Agencia_Promotor_list"),
    path("Agencia/Promotor/create/", views.PromotorCreateView.as_view(), name="Agencia_Promotor_create"),
    path("Agencia/Promotor/detail/<int:idPromotor>/", views.PromotorDetailView.as_view(), name="Agencia_Promotor_detail"),
    path("Agencia/Promotor/update/<int:idPromotor>/", views.PromotorUpdateView.as_view(), name="Agencia_Promotor_update"),
    path("Agencia/Promotor/delete/<int:idPromotor>/", views.PromotorDeleteView.as_view(), name="Agencia_Promotor_delete"),
    path("Agencia/PlanImagen/", views.PlanImagenListView.as_view(), name="Agencia_PlanImagen_list"),
    path("Agencia/PlanImagen/create/", views.PlanImagenCreateView.as_view(), name="Agencia_PlanImagen_create"),
    path("Agencia/PlanImagen/detail/<int:idPlanImagen>/", views.PlanImagenDetailView.as_view(), name="Agencia_PlanImagen_detail"),
    path("Agencia/PlanImagen/update/<int:idPlanImagen>/", views.PlanImagenUpdateView.as_view(), name="Agencia_PlanImagen_update"),
    path("Agencia/PlanImagen/delete/<int:idPlanImagen>/", views.PlanImagenDeleteView.as_view(), name="Agencia_PlanImagen_delete"),
    path("Agencia/Estado/", views.EstadoListView.as_view(), name="Agencia_Estado_list"),
    path("Agencia/Estado/create/", views.EstadoCreateView.as_view(), name="Agencia_Estado_create"),
    path("Agencia/Estado/detail/<int:idEstado>/", views.EstadoDetailView.as_view(), name="Agencia_Estado_detail"),
    path("Agencia/Estado/update/<int:idEstado>/", views.EstadoUpdateView.as_view(), name="Agencia_Estado_update"),
    path("Agencia/Estado/delete/<int:idEstado>/", views.EstadoDeleteView.as_view(), name="Agencia_Estado_delete"),
    path("Agencia/TransaccionPlan/", views.TransaccionPlanListView.as_view(), name="Agencia_TransaccionPlan_list"),
    path("Agencia/TransaccionPlan/create/", views.TransaccionPlanCreateView.as_view(), name="Agencia_TransaccionPlan_create"),
    path("Agencia/TransaccionPlan/detail/<int:idTransaccionPlan>/", views.TransaccionPlanDetailView.as_view(), name="Agencia_TransaccionPlan_detail"),
    path("Agencia/TransaccionPlan/update/<int:idTransaccionPlan>/", views.TransaccionPlanUpdateView.as_view(), name="Agencia_TransaccionPlan_update"),
    path("Agencia/TransaccionPlan/delete/<int:idTransaccionPlan>/", views.TransaccionPlanDeleteView.as_view(), name="Agencia_TransaccionPlan_delete"),
    # path("Agencia/TipoParentesco/", views.TipoParentescoListView.as_view(), name="Agencia_TipoParentesco_list"),
    # path("Agencia/TipoParentesco/create/", views.TipoParentescoCreateView.as_view(), name="Agencia_TipoParentesco_create"),
    # path("Agencia/TipoParentesco/detail/<int:idTipoParentesco>/", views.TipoParentescoDetailView.as_view(), name="Agencia_TipoParentesco_detail"),
    # path("Agencia/TipoParentesco/update/<int:idTipoParentesco>/", views.TipoParentescoUpdateView.as_view(), name="Agencia_TipoParentesco_update"),
    # path("Agencia/TipoParentesco/delete/<int:idTipoParentesco>/", views.TipoParentescoDeleteView.as_view(), name="Agencia_TipoParentesco_delete"),
    path("Agencia/TipoDocumento/", views.TipoDocumentoListView.as_view(), name="Agencia_TipoDocumento_list"),
    path("Agencia/TipoDocumento/create/", views.TipoDocumentoCreateView.as_view(), name="Agencia_TipoDocumento_create"),
    path("Agencia/TipoDocumento/detail/<int:idTipoDocumento>/", views.TipoDocumentoDetailView.as_view(), name="Agencia_TipoDocumento_detail"),
    path("Agencia/TipoDocumento/update/<int:idTipoDocumento>/", views.TipoDocumentoUpdateView.as_view(), name="Agencia_TipoDocumento_update"),
    path("Agencia/TipoDocumento/delete/<int:idTipoDocumento>/", views.TipoDocumentoDeleteView.as_view(), name="Agencia_TipoDocumento_delete"),
    path("Agencia/Promocion/", views.PromocionListView.as_view(), name="Agencia_Promocion_list"),
    path("Agencia/Promocion/create/", views.PromocionCreateView.as_view(), name="Agencia_Promocion_create"),
    path("Agencia/Promocion/detail/<int:idPromocion>/", views.PromocionDetailView.as_view(), name="Agencia_Promocion_detail"),
    path("Agencia/Promocion/update/<int:idPromocion>/", views.PromocionUpdateView.as_view(), name="Agencia_Promocion_update"),
    path("Agencia/Promocion/delete/<int:idPromocion>/", views.PromocionDeleteView.as_view(), name="Agencia_Promocion_delete"),
    path("Agencia/TipoPQRS/", views.TipoPQRSListView.as_view(), name="Agencia_TipoPQRS_list"),
    path("Agencia/TipoPQRS/create/", views.TipoPQRSCreateView.as_view(), name="Agencia_TipoPQRS_create"),
    path("Agencia/TipoPQRS/detail/<int:idTipoPQRS>/", views.TipoPQRSDetailView.as_view(), name="Agencia_TipoPQRS_detail"),
    path("Agencia/TipoPQRS/update/<int:idTipoPQRS>/", views.TipoPQRSUpdateView.as_view(), name="Agencia_TipoPQRS_update"),
    path("Agencia/TipoPQRS/delete/<int:idTipoPQRS>/", views.TipoPQRSDeleteView.as_view(), name="Agencia_TipoPQRS_delete"),
    # path("Agencia/Integrante/", views.IntegranteListView.as_view(), name="Agencia_Integrante_list"),
    # path("Agencia/Integrante/create/", views.IntegranteCreateView.as_view(), name="Agencia_Integrante_create"),
    # path("Agencia/Integrante/detail/<int:idIntegrante>/", views.IntegranteDetailView.as_view(), name="Agencia_Integrante_detail"),
    # path("Agencia/Integrante/update/<int:idIntegrante>/", views.IntegranteUpdateView.as_view(), name="Agencia_Integrante_update"),
    # path("Agencia/Integrante/delete/<int:idIntegrante>/", views.IntegranteDeleteView.as_view(), name="Agencia_Integrante_delete"),
    # path("Agencia/Transaccion/", views.TransaccionListView.as_view(), name="Agencia_Transaccion_list"),
    # path("Agencia/Transaccion/create/", views.TransaccionCreateView.as_view(), name="Agencia_Transaccion_create"),
    # path("Agencia/Transaccion/detail/<int:idTransaccion>/", views.TransaccionDetailView.as_view(), name="Agencia_Transaccion_detail"),
    # path("Agencia/Transaccion/update/<int:idTransaccion>/", views.TransaccionUpdateView.as_view(), name="Agencia_Transaccion_update"),
    # path("Agencia/Transaccion/delete/<int:idTransaccion>/", views.TransaccionDeleteView.as_view(), name="Agencia_Transaccion_delete"),
    path("Agencia/Ciudad/", views.CiudadListView.as_view(), name="Agencia_Ciudad_list"),
    path("Agencia/Ciudad/create/", views.CiudadCreateView.as_view(), name="Agencia_Ciudad_create"),
    path("Agencia/Ciudad/detail/<int:idCiudad>/", views.CiudadDetailView.as_view(), name="Agencia_Ciudad_detail"),
    path("Agencia/Ciudad/update/<int:idCiudad>/", views.CiudadUpdateView.as_view(), name="Agencia_Ciudad_update"),
    path("Agencia/Ciudad/delete/<int:idCiudad>/", views.CiudadDeleteView.as_view(), name="Agencia_Ciudad_delete"),
    # path("Agencia/PQRS/", views.PQRSListView.as_view(), name="Agencia_PQRS_list"),
    # path("Agencia/PQRS/create/", views.PQRSCreateView.as_view(), name="Agencia_PQRS_create"),
    # path("Agencia/PQRS/detail/<int:pk>/", views.PQRSDetailView.as_view(), name="Agencia_PQRS_detail"),
    # path("Agencia/PQRS/update/<int:pk>/", views.PQRSUpdateView.as_view(), name="Agencia_PQRS_update"),
    # path("Agencia/PQRS/delete/<int:pk>/", views.PQRSDeleteView.as_view(), name="Agencia_PQRS_delete"),
    path("Agencia/TransaccionPromocion/", views.TransaccionPromocionListView.as_view(), name="Agencia_TransaccionPromocion_list"),
    path("Agencia/TransaccionPromocion/create/", views.TransaccionPromocionCreateView.as_view(), name="Agencia_TransaccionPromocion_create"),
    path("Agencia/TransaccionPromocion/detail/<int:idTransaccionPromocion>/", views.TransaccionPromocionDetailView.as_view(), name="Agencia_TransaccionPromocion_detail"),
    path("Agencia/TransaccionPromocion/update/<int:idTransaccionPromocion>/", views.TransaccionPromocionUpdateView.as_view(), name="Agencia_TransaccionPromocion_update"),
    path("Agencia/TransaccionPromocion/delete/<int:idTransaccionPromocion>/", views.TransaccionPromocionDeleteView.as_view(), name="Agencia_TransaccionPromocion_delete"),
    path("Agencia/Pais/", views.PaisListView.as_view(), name="Agencia_Pais_list"),
    path("Agencia/Pais/create/", views.PaisCreateView.as_view(), name="Agencia_Pais_create"),
    path("Agencia/Pais/detail/<int:idPais>/", views.PaisDetailView.as_view(), name="Agencia_Pais_detail"),
    path("Agencia/Pais/update/<int:idPais>/", views.PaisUpdateView.as_view(), name="Agencia_Pais_update"),
    path("Agencia/Pais/delete/<int:idPais>/", views.PaisDeleteView.as_view(), name="Agencia_Pais_delete"),
    path("Agencia/Cupon/", views.CuponListView.as_view(), name="Agencia_Cupon_list"),
    path("Agencia/Cupon/create/", views.CuponCreateView.as_view(), name="Agencia_Cupon_create"),
    path("Agencia/Cupon/detail/<int:idCupon>/", views.CuponDetailView.as_view(), name="Agencia_Cupon_detail"),
    path("Agencia/Cupon/update/<int:idCupon>/", views.CuponUpdateView.as_view(), name="Agencia_Cupon_update"),
    path("Agencia/Cupon/delete/<int:idCupon>/", views.CuponDeleteView.as_view(), name="Agencia_Cupon_delete"),
    path("Agencia/Imagen/", views.ImagenListView.as_view(), name="Agencia_Imagen_list"),
    path("Agencia/Imagen/create/", views.ImagenCreateView.as_view(), name="Agencia_Imagen_create"),
    path("Agencia/Imagen/detail/<int:idImagen>/", views.ImagenDetailView.as_view(), name="Agencia_Imagen_detail"),
    path("Agencia/Imagen/update/<int:idImagen>/", views.ImagenUpdateView.as_view(), name="Agencia_Imagen_update"),
    path("Agencia/Imagen/delete/<int:idImagen>/", views.ImagenDeleteView.as_view(), name="Agencia_Imagen_delete"),
    path("Agencia/PromocionImagen/", views.PromocionImagenListView.as_view(), name="Agencia_PromocionImagen_list"),
    path("Agencia/PromocionImagen/create/", views.PromocionImagenCreateView.as_view(), name="Agencia_PromocionImagen_create"),
    path("Agencia/PromocionImagen/detail/<int:idPromocionImagen>/", views.PromocionImagenDetailView.as_view(), name="Agencia_PromocionImagen_detail"),
    path("Agencia/PromocionImagen/update/<int:idPromocionImagen>/", views.PromocionImagenUpdateView.as_view(), name="Agencia_PromocionImagen_update"),
    path("Agencia/PromocionImagen/delete/<int:idPromocionImagen>/", views.PromocionImagenDeleteView.as_view(), name="Agencia_PromocionImagen_delete"),
    path("Agencia/PlanTuristico/", views.PlanTuristicoListView.as_view(), name="Agencia_PlanTuristico_list"),
    path("Agencia/PlanTuristico/create/", views.PlanTuristicoCreateView.as_view(), name="Agencia_PlanTuristico_create"),
    path("Agencia/PlanTuristico/detail/<int:idPlan>/", views.PlanTuristicoDetailView.as_view(), name="Agencia_PlanTuristico_detail"),
    path("Agencia/PlanTuristico/update/<int:idPlan>/", views.PlanTuristicoUpdateView.as_view(), name="Agencia_PlanTuristico_update"),
    path("Agencia/PlanTuristico/delete/<int:idPlan>/", views.PlanTuristicoDeleteView.as_view(), name="Agencia_PlanTuristico_delete"),
    path("Agencia/Cliente/", views.ClienteListView.as_view(), name="Agencia_Cliente_list"),
    path("Agencia/Cliente/create/", views.ClienteCreateView.as_view(), name="Agencia_Cliente_create"),
    path("Agencia/Cliente/detail/<int:idCliente>/", views.ClienteDetailView.as_view(), name="Agencia_Cliente_detail"),
    path("Agencia/Cliente/update/<int:idCliente>/", views.ClienteUpdateView.as_view(), name="Agencia_Cliente_update"),
    path("Agencia/Cliente/delete/<int:idCliente>/", views.ClienteDeleteView.as_view(), name="Agencia_Cliente_delete"),
)
