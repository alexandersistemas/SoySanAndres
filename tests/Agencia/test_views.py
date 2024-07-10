import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Promotor_list_view():
    instance1 = test_helpers.create_Agencia_Promotor()
    instance2 = test_helpers.create_Agencia_Promotor()
    client = Client()
    url = reverse("Agencia_Promotor_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Promotor_create_view():
    idTipoDocumento = test_helpers.create_Agencia_TipoDocumento()
    client = Client()
    url = reverse("Agencia_Promotor_create")
    data = {
        "Nombres": "text",
        "PorcentajeComision": 1,
        "NumeroDocumento": 1,
        "Apellidos": "text",
        "idTipoDocumento": idTipoDocumento.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Promotor_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_Promotor()
    url = reverse("Agencia_Promotor_detail", args=[instance.idPromotor, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Promotor_update_view():
    idTipoDocumento = test_helpers.create_Agencia_TipoDocumento()
    client = Client()
    instance = test_helpers.create_Agencia_Promotor()
    url = reverse("Agencia_Promotor_update", args=[instance.idPromotor, ])
    data = {
        "Nombres": "text",
        "PorcentajeComision": 1,
        "NumeroDocumento": 1,
        "Apellidos": "text",
        "idTipoDocumento": idTipoDocumento.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanImagen_list_view():
    instance1 = test_helpers.create_Agencia_PlanImagen()
    instance2 = test_helpers.create_Agencia_PlanImagen()
    client = Client()
    url = reverse("Agencia_PlanImagen_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_PlanImagen_create_view():
    idPlan = test_helpers.create_Agencia_PlanTuristico()
    idImagen = test_helpers.create_Agencia_Imagen()
    client = Client()
    url = reverse("Agencia_PlanImagen_create")
    data = {
        "idPlan": idPlan.pk,
        "idImagen": idImagen.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanImagen_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_PlanImagen()
    url = reverse("Agencia_PlanImagen_detail", args=[instance.idPlanImagen, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_PlanImagen_update_view():
    idPlan = test_helpers.create_Agencia_PlanTuristico()
    idImagen = test_helpers.create_Agencia_Imagen()
    client = Client()
    instance = test_helpers.create_Agencia_PlanImagen()
    url = reverse("Agencia_PlanImagen_update", args=[instance.idPlanImagen, ])
    data = {
        "idPlan": idPlan.pk,
        "idImagen": idImagen.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Estado_list_view():
    instance1 = test_helpers.create_Agencia_Estado()
    instance2 = test_helpers.create_Agencia_Estado()
    client = Client()
    url = reverse("Agencia_Estado_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Estado_create_view():
    client = Client()
    url = reverse("Agencia_Estado_create")
    data = {
        "Nombre": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Estado_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_Estado()
    url = reverse("Agencia_Estado_detail", args=[instance.idEstado, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Estado_update_view():
    client = Client()
    instance = test_helpers.create_Agencia_Estado()
    url = reverse("Agencia_Estado_update", args=[instance.idEstado, ])
    data = {
        "Nombre": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TransaccionPlan_list_view():
    instance1 = test_helpers.create_Agencia_TransaccionPlan()
    instance2 = test_helpers.create_Agencia_TransaccionPlan()
    client = Client()
    url = reverse("Agencia_TransaccionPlan_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_TransaccionPlan_create_view():
    idTransaccion = test_helpers.create_Agencia_Transaccion()
    idPlan = test_helpers.create_Agencia_PlanTuristico()
    client = Client()
    url = reverse("Agencia_TransaccionPlan_create")
    data = {
        "idTransaccion": idTransaccion.pk,
        "idPlan": idPlan.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TransaccionPlan_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_TransaccionPlan()
    url = reverse("Agencia_TransaccionPlan_detail", args=[instance.idTransaccionPlan, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_TransaccionPlan_update_view():
    idTransaccion = test_helpers.create_Agencia_Transaccion()
    idPlan = test_helpers.create_Agencia_PlanTuristico()
    client = Client()
    instance = test_helpers.create_Agencia_TransaccionPlan()
    url = reverse("Agencia_TransaccionPlan_update", args=[instance.idTransaccionPlan, ])
    data = {
        "idTransaccion": idTransaccion.pk,
        "idPlan": idPlan.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TipoDocumento_list_view():
    instance1 = test_helpers.create_Agencia_TipoDocumento()
    instance2 = test_helpers.create_Agencia_TipoDocumento()
    client = Client()
    url = reverse("Agencia_TipoDocumento_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_TipoDocumento_create_view():
    client = Client()
    url = reverse("Agencia_TipoDocumento_create")
    data = {
        "Nombre": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TipoDocumento_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_TipoDocumento()
    url = reverse("Agencia_TipoDocumento_detail", args=[instance.idTipoDocumento, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_TipoDocumento_update_view():
    client = Client()
    instance = test_helpers.create_Agencia_TipoDocumento()
    url = reverse("Agencia_TipoDocumento_update", args=[instance.idTipoDocumento, ])
    data = {
        "Nombre": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Promocion_list_view():
    instance1 = test_helpers.create_Agencia_Promocion()
    instance2 = test_helpers.create_Agencia_Promocion()
    client = Client()
    url = reverse("Agencia_Promocion_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Promocion_create_view():
    client = Client()
    url = reverse("Agencia_Promocion_create")
    data = {
        "FechaInicio": datetime.now(),
        "Nombre": "text",
        "PrecioPeso": 1,
        "Descripcion": "text",
        "FechaFin": datetime.now(),
        "PrecioDolar": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Promocion_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_Promocion()
    url = reverse("Agencia_Promocion_detail", args=[instance.idPromocion, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Promocion_update_view():
    client = Client()
    instance = test_helpers.create_Agencia_Promocion()
    url = reverse("Agencia_Promocion_update", args=[instance.idPromocion, ])
    data = {
        "FechaInicio": datetime.now(),
        "Nombre": "text",
        "PrecioPeso": 1,
        "Descripcion": "text",
        "FechaFin": datetime.now(),
        "PrecioDolar": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TipoPQRS_list_view():
    instance1 = test_helpers.create_Agencia_TipoPQRS()
    instance2 = test_helpers.create_Agencia_TipoPQRS()
    client = Client()
    url = reverse("Agencia_TipoPQRS_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_TipoPQRS_create_view():
    client = Client()
    url = reverse("Agencia_TipoPQRS_create")
    data = {
        "Nombre": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TipoPQRS_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_TipoPQRS()
    url = reverse("Agencia_TipoPQRS_detail", args=[instance.idTipoPQRS, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_TipoPQRS_update_view():
    client = Client()
    instance = test_helpers.create_Agencia_TipoPQRS()
    url = reverse("Agencia_TipoPQRS_update", args=[instance.idTipoPQRS, ])
    data = {
        "Nombre": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Transaccion_list_view():
    instance1 = test_helpers.create_Agencia_Transaccion()
    instance2 = test_helpers.create_Agencia_Transaccion()
    client = Client()
    url = reverse("Agencia_Transaccion_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Transaccion_create_view():
    idCupon = test_helpers.create_Agencia_Cupon()
    idEstado = test_helpers.create_Agencia_Estado()
    idCliente = test_helpers.create_Agencia_Cliente()
    idPromotor = test_helpers.create_Agencia_Promotor()
    client = Client()
    url = reverse("Agencia_Transaccion_create")
    data = {
        "Valor": 1,
        "idCupon": idCupon.pk,
        "idEstado": idEstado.pk,
        "idCliente": idCliente.pk,
        "idPromotor": idPromotor.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Transaccion_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_Transaccion()
    url = reverse("Agencia_Transaccion_detail", args=[instance.idTransaccion, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Transaccion_update_view():
    idCupon = test_helpers.create_Agencia_Cupon()
    idEstado = test_helpers.create_Agencia_Estado()
    idCliente = test_helpers.create_Agencia_Cliente()
    idPromotor = test_helpers.create_Agencia_Promotor()
    client = Client()
    instance = test_helpers.create_Agencia_Transaccion()
    url = reverse("Agencia_Transaccion_update", args=[instance.idTransaccion, ])
    data = {
        "Valor": 1,
        "idCupon": idCupon.pk,
        "idEstado": idEstado.pk,
        "idCliente": idCliente.pk,
        "idPromotor": idPromotor.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ciudad_list_view():
    instance1 = test_helpers.create_Agencia_Ciudad()
    instance2 = test_helpers.create_Agencia_Ciudad()
    client = Client()
    url = reverse("Agencia_Ciudad_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Ciudad_create_view():
    idPais = test_helpers.create_Agencia_Pais()
    client = Client()
    url = reverse("Agencia_Ciudad_create")
    data = {
        "Nombre": "text",
        "idPais": idPais.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Ciudad_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_Ciudad()
    url = reverse("Agencia_Ciudad_detail", args=[instance.idCiudad, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Ciudad_update_view():
    idPais = test_helpers.create_Agencia_Pais()
    client = Client()
    instance = test_helpers.create_Agencia_Ciudad()
    url = reverse("Agencia_Ciudad_update", args=[instance.idCiudad, ])
    data = {
        "Nombre": "text",
        "idPais": idPais.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PQRS_list_view():
    instance1 = test_helpers.create_Agencia_PQRS()
    instance2 = test_helpers.create_Agencia_PQRS()
    client = Client()
    url = reverse("Agencia_PQRS_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_PQRS_create_view():
    idTipoPQRS = test_helpers.create_Agencia_TipoPQRS()
    idCliente = test_helpers.create_Agencia_Cliente()
    client = Client()
    url = reverse("Agencia_PQRS_create")
    data = {
        "Descripcion": "text",
        "idTipoPQRS": idTipoPQRS.pk,
        "idCliente": idCliente.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PQRS_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_PQRS()
    url = reverse("Agencia_PQRS_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_PQRS_update_view():
    idTipoPQRS = test_helpers.create_Agencia_TipoPQRS()
    idCliente = test_helpers.create_Agencia_Cliente()
    client = Client()
    instance = test_helpers.create_Agencia_PQRS()
    url = reverse("Agencia_PQRS_update", args=[instance.pk, ])
    data = {
        "Descripcion": "text",
        "idTipoPQRS": idTipoPQRS.pk,
        "idCliente": idCliente.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TransaccionPromocion_list_view():
    instance1 = test_helpers.create_Agencia_TransaccionPromocion()
    instance2 = test_helpers.create_Agencia_TransaccionPromocion()
    client = Client()
    url = reverse("Agencia_TransaccionPromocion_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_TransaccionPromocion_create_view():
    idPromocion = test_helpers.create_Agencia_Promocion()
    idTransaccion = test_helpers.create_Agencia_Transaccion()
    client = Client()
    url = reverse("Agencia_TransaccionPromocion_create")
    data = {
        "idPromocion": idPromocion.pk,
        "idTransaccion": idTransaccion.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_TransaccionPromocion_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_TransaccionPromocion()
    url = reverse("Agencia_TransaccionPromocion_detail", args=[instance.idTransaccionPromocion, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_TransaccionPromocion_update_view():
    idPromocion = test_helpers.create_Agencia_Promocion()
    idTransaccion = test_helpers.create_Agencia_Transaccion()
    client = Client()
    instance = test_helpers.create_Agencia_TransaccionPromocion()
    url = reverse("Agencia_TransaccionPromocion_update", args=[instance.idTransaccionPromocion, ])
    data = {
        "idPromocion": idPromocion.pk,
        "idTransaccion": idTransaccion.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Pais_list_view():
    instance1 = test_helpers.create_Agencia_Pais()
    instance2 = test_helpers.create_Agencia_Pais()
    client = Client()
    url = reverse("Agencia_Pais_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Pais_create_view():
    client = Client()
    url = reverse("Agencia_Pais_create")
    data = {
        "Nombre": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Pais_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_Pais()
    url = reverse("Agencia_Pais_detail", args=[instance.idPais, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Pais_update_view():
    client = Client()
    instance = test_helpers.create_Agencia_Pais()
    url = reverse("Agencia_Pais_update", args=[instance.idPais, ])
    data = {
        "Nombre": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Cupon_list_view():
    instance1 = test_helpers.create_Agencia_Cupon()
    instance2 = test_helpers.create_Agencia_Cupon()
    client = Client()
    url = reverse("Agencia_Cupon_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Cupon_create_view():
    client = Client()
    url = reverse("Agencia_Cupon_create")
    data = {
        "Porcentaje": 1,
        "Cupon": "text",
        "FechaInicio": datetime.now(),
        "FechaFin": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Cupon_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_Cupon()
    url = reverse("Agencia_Cupon_detail", args=[instance.idCupon, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Cupon_update_view():
    client = Client()
    instance = test_helpers.create_Agencia_Cupon()
    url = reverse("Agencia_Cupon_update", args=[instance.idCupon, ])
    data = {
        "Porcentaje": 1,
        "Cupon": "text",
        "FechaInicio": datetime.now(),
        "FechaFin": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Imagen_list_view():
    instance1 = test_helpers.create_Agencia_Imagen()
    instance2 = test_helpers.create_Agencia_Imagen()
    client = Client()
    url = reverse("Agencia_Imagen_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Imagen_create_view():
    client = Client()
    url = reverse("Agencia_Imagen_create")
    data = {
        "Ruta": "text",
        "Nombre": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Imagen_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_Imagen()
    url = reverse("Agencia_Imagen_detail", args=[instance.idImagen, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Imagen_update_view():
    client = Client()
    instance = test_helpers.create_Agencia_Imagen()
    url = reverse("Agencia_Imagen_update", args=[instance.idImagen, ])
    data = {
        "Ruta": "text",
        "Nombre": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PromocionImagen_list_view():
    instance1 = test_helpers.create_Agencia_PromocionImagen()
    instance2 = test_helpers.create_Agencia_PromocionImagen()
    client = Client()
    url = reverse("Agencia_PromocionImagen_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_PromocionImagen_create_view():
    idImagen = test_helpers.create_Agencia_Imagen()
    idPromocion = test_helpers.create_Agencia_Promocion()
    client = Client()
    url = reverse("Agencia_PromocionImagen_create")
    data = {
        "idImagen": idImagen.pk,
        "idPromocion": idPromocion.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PromocionImagen_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_PromocionImagen()
    url = reverse("Agencia_PromocionImagen_detail", args=[instance.idPromocionImagen, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_PromocionImagen_update_view():
    idImagen = test_helpers.create_Agencia_Imagen()
    idPromocion = test_helpers.create_Agencia_Promocion()
    client = Client()
    instance = test_helpers.create_Agencia_PromocionImagen()
    url = reverse("Agencia_PromocionImagen_update", args=[instance.idPromocionImagen, ])
    data = {
        "idImagen": idImagen.pk,
        "idPromocion": idPromocion.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanTuristico_list_view():
    instance1 = test_helpers.create_Agencia_PlanTuristico()
    instance2 = test_helpers.create_Agencia_PlanTuristico()
    client = Client()
    url = reverse("Agencia_PlanTuristico_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_PlanTuristico_create_view():
    client = Client()
    url = reverse("Agencia_PlanTuristico_create")
    data = {
        "Descripcion": "text",
        "Capacidad": 1,
        "Nombre": "text",
        "PrecioDolar": 1,
        "PrecioPeso": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_PlanTuristico_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_PlanTuristico()
    url = reverse("Agencia_PlanTuristico_detail", args=[instance.idPlan, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_PlanTuristico_update_view():
    client = Client()
    instance = test_helpers.create_Agencia_PlanTuristico()
    url = reverse("Agencia_PlanTuristico_update", args=[instance.idPlan, ])
    data = {
        "Descripcion": "text",
        "Capacidad": 1,
        "Nombre": "text",
        "PrecioDolar": 1,
        "PrecioPeso": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Cliente_list_view():
    instance1 = test_helpers.create_Agencia_Cliente()
    instance2 = test_helpers.create_Agencia_Cliente()
    client = Client()
    url = reverse("Agencia_Cliente_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Cliente_create_view():
    idCiudad = test_helpers.create_Agencia_Ciudad()
    idTipoDocumento = test_helpers.create_Agencia_TipoDocumento()
    client = Client()
    url = reverse("Agencia_Cliente_create")
    data = {
        "Telefono2": "text",
        "Direccion": "text",
        "Telefono1": "text",
        "FechaNacimiento": datetime.now(),
        "NumeroDocumento": 1,
        "Correo": "user@tempurl.com",
        "Apellidos": "text",
        "Nombres": "text",
        "idCiudad": idCiudad.pk,
        "idTipoDocumento": idTipoDocumento.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Cliente_detail_view():
    client = Client()
    instance = test_helpers.create_Agencia_Cliente()
    url = reverse("Agencia_Cliente_detail", args=[instance.idCliente, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Cliente_update_view():
    idCiudad = test_helpers.create_Agencia_Ciudad()
    idTipoDocumento = test_helpers.create_Agencia_TipoDocumento()
    client = Client()
    instance = test_helpers.create_Agencia_Cliente()
    url = reverse("Agencia_Cliente_update", args=[instance.idCliente, ])
    data = {
        "Telefono2": "text",
        "Direccion": "text",
        "Telefono1": "text",
        "FechaNacimiento": datetime.now(),
        "NumeroDocumento": 1,
        "Correo": "user@tempurl.com",
        "Apellidos": "text",
        "Nombres": "text",
        "idCiudad": idCiudad.pk,
        "idTipoDocumento": idTipoDocumento.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
