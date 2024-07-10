import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from Agencia import models as Agencia_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_Agencia_Promotor(**kwargs):
    defaults = {}
    defaults["Nombres"] = ""
    defaults["PorcentajeComision"] = ""
    defaults["NumeroDocumento"] = ""
    defaults["Apellidos"] = ""
    if "idTipoDocumento" not in kwargs:
        defaults["idTipoDocumento"] = create_Agencia_TipoDocumento()
    defaults.update(**kwargs)
    return Agencia_models.Promotor.objects.create(**defaults)
def create_Agencia_PlanImagen(**kwargs):
    defaults = {}
    if "idPlan" not in kwargs:
        defaults["idPlan"] = create_Agencia_PlanTuristico()
    if "idImagen" not in kwargs:
        defaults["idImagen"] = create_Agencia_Imagen()
    defaults.update(**kwargs)
    return Agencia_models.PlanImagen.objects.create(**defaults)
def create_Agencia_Estado(**kwargs):
    defaults = {}
    defaults["Nombre"] = ""
    defaults.update(**kwargs)
    return Agencia_models.Estado.objects.create(**defaults)
def create_Agencia_TransaccionPlan(**kwargs):
    defaults = {}
    if "idTransaccion" not in kwargs:
        defaults["idTransaccion"] = create_Agencia_Transaccion()
    if "idPlan" not in kwargs:
        defaults["idPlan"] = create_Agencia_PlanTuristico()
    defaults.update(**kwargs)
    return Agencia_models.TransaccionPlan.objects.create(**defaults)
def create_Agencia_TipoDocumento(**kwargs):
    defaults = {}
    defaults["Nombre"] = ""
    defaults.update(**kwargs)
    return Agencia_models.TipoDocumento.objects.create(**defaults)
def create_Agencia_Promocion(**kwargs):
    defaults = {}
    defaults["FechaInicio"] = datetime.now()
    defaults["Nombre"] = ""
    defaults["PrecioPeso"] = ""
    defaults["Descripcion"] = ""
    defaults["FechaFin"] = datetime.now()
    defaults["PrecioDolar"] = ""
    defaults.update(**kwargs)
    return Agencia_models.Promocion.objects.create(**defaults)
def create_Agencia_TipoPQRS(**kwargs):
    defaults = {}
    defaults["Nombre"] = ""
    defaults.update(**kwargs)
    return Agencia_models.TipoPQRS.objects.create(**defaults)
def create_Agencia_Transaccion(**kwargs):
    defaults = {}
    defaults["Valor"] = ""
    if "idCupon" not in kwargs:
        defaults["idCupon"] = create_Agencia_Cupon()
    if "idEstado" not in kwargs:
        defaults["idEstado"] = create_Agencia_Estado()

    if "idPromotor" not in kwargs:
        defaults["idPromotor"] = create_Agencia_Promotor()
    defaults.update(**kwargs)
    return Agencia_models.Transaccion.objects.create(**defaults)
def create_Agencia_Ciudad(**kwargs):
    defaults = {}
    defaults["Nombre"] = ""
    if "idPais" not in kwargs:
        defaults["idPais"] = create_Agencia_Pais()
    defaults.update(**kwargs)
    return Agencia_models.Ciudad.objects.create(**defaults)
def create_Agencia_PQRS(**kwargs):
    defaults = {}
    defaults["Descripcion"] = ""
    if "idTipoPQRS" not in kwargs:
        defaults["idTipoPQRS"] = create_Agencia_TipoPQRS()

    defaults.update(**kwargs)
    return Agencia_models.PQRS.objects.create(**defaults)
def create_Agencia_TransaccionPromocion(**kwargs):
    defaults = {}
    if "idPromocion" not in kwargs:
        defaults["idPromocion"] = create_Agencia_Promocion()
    if "idTransaccion" not in kwargs:
        defaults["idTransaccion"] = create_Agencia_Transaccion()
    defaults.update(**kwargs)
    return Agencia_models.TransaccionPromocion.objects.create(**defaults)
def create_Agencia_Pais(**kwargs):
    defaults = {}
    defaults["Nombre"] = ""
    defaults.update(**kwargs)
    return Agencia_models.Pais.objects.create(**defaults)
def create_Agencia_Cupon(**kwargs):
    defaults = {}
    defaults["Porcentaje"] = ""
    defaults["Cupon"] = ""
    defaults["FechaInicio"] = datetime.now()
    defaults["FechaFin"] = datetime.now()
    defaults.update(**kwargs)
    return Agencia_models.Cupon.objects.create(**defaults)
def create_Agencia_Imagen(**kwargs):
    defaults = {}
    defaults["Ruta"] = ""
    defaults["Nombre"] = ""
    defaults.update(**kwargs)
    return Agencia_models.Imagen.objects.create(**defaults)
def create_Agencia_PromocionImagen(**kwargs):
    defaults = {}
    if "idImagen" not in kwargs:
        defaults["idImagen"] = create_Agencia_Imagen()
    if "idPromocion" not in kwargs:
        defaults["idPromocion"] = create_Agencia_Promocion()
    defaults.update(**kwargs)
    return Agencia_models.PromocionImagen.objects.create(**defaults)
def create_Agencia_PlanTuristico(**kwargs):
    defaults = {}
    defaults["Descripcion"] = ""
    defaults["Capacidad"] = ""
    defaults["Nombre"] = ""
    defaults["PrecioDolar"] = ""
    defaults["PrecioPeso"] = ""
    defaults.update(**kwargs)
    return Agencia_models.PlanTuristico.objects.create(**defaults)
def create_Agencia_Cliente(**kwargs):
    defaults = {}
    defaults["Telefono2"] = ""
    defaults["Direccion"] = ""
    defaults["Telefono1"] = ""
    defaults["FechaNacimiento"] = datetime.now()
    defaults["NumeroDocumento"] = ""
    defaults["Correo"] = ""
    defaults["Apellidos"] = ""
    defaults["Nombres"] = ""
    if "idCiudad" not in kwargs:
        defaults["idCiudad"] = create_Agencia_Ciudad()
    if "idTipoDocumento" not in kwargs:
        defaults["idTipoDocumento"] = create_Agencia_TipoDocumento()
    defaults.update(**kwargs)
    return Agencia_models.Cliente.objects.create(**defaults)
