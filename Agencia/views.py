from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from . import models
from .forms import ClienteForm
from django.contrib import messages
from . import forms

#Cuando desde el formulario de usuario se da guardar este
def create_client(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente = form.save(commit=False)
            Cliente.idCiudad = request.POST['idCiudad']
            Cliente.idTipoDocumento = request.POST['idTipoDocumento']
            Cliente.Nombres = request.POST['Nombres']
            Cliente.Apellidos =request.POST['Apellidos']
            Cliente.FechaNacimiento = request.POST['FechaNacimiento']
            Cliente.Direccion = request.POST['Direccion']
            Cliente.Telefono1 = request.POST['Telefono1']
            Cliente.Telefono2 = request.POST['Telefono2']
            Cliente.Correo = request.POST['Correo']
            Cliente.Password = request.POST['Password']
            Cliente.save()

            messages.success(request, 'Guardado!')
            return redirect('Agencia/Registro/')

        else:
            messages.error(request, form.errors)
            return redirect('Agencia/Registro/')
    else:
        form = ClienteForm()
        return redirect('Agencia/Registro/')


def formularioRegistro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente = form.save(commit=False)
            Cliente.idCiudad = request.POST['idCiudad']
            Cliente.idTipoDocumento = request.POST['idTipoDocumento']
            Cliente.Nombres = request.POST['Nombres']
            Cliente.Apellidos =request.POST['Apellidos']
            Cliente.FechaNacimiento = request.POST['FechaNacimiento']
            Cliente.Direccion = request.POST['Direccion']
            Cliente.Telefono1 = request.POST['Telefono1']
            Cliente.Telefono2 = request.POST['Telefono2']
            Cliente.Correo = request.POST['Correo']
            Cliente.Password = request.POST['Password']
            Cliente.save()

            messages.success(request, 'Guardado!')
            return redirect('Agencia/Registro/')

        else:
            messages.error(request, form.errors)
            return redirect('Agencia/Registro/')
    else:
        resultsTipoDoc  = models.TipoDocumento.objects.all()
        resultsPais     = models.Pais.objects.all().order_by('Nombre')
        resultsCiudad = models.Ciudad.objects.all()
        return render(request, "Registro.html",
                          context={'tipodoc': resultsTipoDoc, 'lstPais': resultsPais,'lstCiudad': resultsCiudad,})

def load_cities(request):
    pais_id = request.GET.get('state')
    cities  = models.Ciudad.objects.filter(idPais=pais_id).order_by('name')
    return render(request,  "Registro.html", {'cities': cities})


class PromotorListView(generic.ListView):
    model = models.Promotor
    form_class = forms.PromotorForm


class PromotorCreateView(generic.CreateView):
    model = models.Promotor
    form_class = forms.PromotorForm


class PromotorDetailView(generic.DetailView):
    model = models.Promotor
    form_class = forms.PromotorForm
    pk_url_kwarg = "idPromotor"


class PromotorUpdateView(generic.UpdateView):
    model = models.Promotor
    form_class = forms.PromotorForm
    pk_url_kwarg = "idPromotor"


class PromotorDeleteView(generic.DeleteView):
    model = models.Promotor
    success_url = reverse_lazy("Agencia_Promotor_list")


class PlanImagenListView(generic.ListView):
    model = models.PlanImagen
    form_class = forms.PlanImagenForm


class PlanImagenCreateView(generic.CreateView):
    model = models.PlanImagen
    form_class = forms.PlanImagenForm


class PlanImagenDetailView(generic.DetailView):
    model = models.PlanImagen
    form_class = forms.PlanImagenForm
    pk_url_kwarg = "idPlanImagen"


class PlanImagenUpdateView(generic.UpdateView):
    model = models.PlanImagen
    form_class = forms.PlanImagenForm
    pk_url_kwarg = "idPlanImagen"


class PlanImagenDeleteView(generic.DeleteView):
    model = models.PlanImagen
    success_url = reverse_lazy("Agencia_PlanImagen_list")


class EstadoListView(generic.ListView):
    model = models.Estado
    form_class = forms.EstadoForm


class EstadoCreateView(generic.CreateView):
    model = models.Estado
    form_class = forms.EstadoForm


class EstadoDetailView(generic.DetailView):
    model = models.Estado
    form_class = forms.EstadoForm
    pk_url_kwarg = "idEstado"


class EstadoUpdateView(generic.UpdateView):
    model = models.Estado
    form_class = forms.EstadoForm
    pk_url_kwarg = "idEstado"


class EstadoDeleteView(generic.DeleteView):
    model = models.Estado
    success_url = reverse_lazy("Agencia_Estado_list")


class TransaccionPlanListView(generic.ListView):
    model = models.TransaccionPlan
    form_class = forms.TransaccionPlanForm


class TransaccionPlanCreateView(generic.CreateView):
    model = models.TransaccionPlan
    form_class = forms.TransaccionPlanForm


class TransaccionPlanDetailView(generic.DetailView):
    model = models.TransaccionPlan
    form_class = forms.TransaccionPlanForm
    pk_url_kwarg = "idTransaccionPlan"


class TransaccionPlanUpdateView(generic.UpdateView):
    model = models.TransaccionPlan
    form_class = forms.TransaccionPlanForm
    pk_url_kwarg = "idTransaccionPlan"


class TransaccionPlanDeleteView(generic.DeleteView):
    model = models.TransaccionPlan
    success_url = reverse_lazy("Agencia_TransaccionPlan_list")


class TipoDocumentoListView(generic.ListView):
    model = models.TipoDocumento
    form_class = forms.TipoDocumentoForm


class TipoDocumentoCreateView(generic.CreateView):
    model = models.TipoDocumento
    form_class = forms.TipoDocumentoForm


class TipoDocumentoDetailView(generic.DetailView):
    model = models.TipoDocumento
    form_class = forms.TipoDocumentoForm
    pk_url_kwarg = "idTipoDocumento"


class TipoDocumentoUpdateView(generic.UpdateView):
    model = models.TipoDocumento
    form_class = forms.TipoDocumentoForm
    pk_url_kwarg = "idTipoDocumento"


class TipoDocumentoDeleteView(generic.DeleteView):
    model = models.TipoDocumento
    success_url = reverse_lazy("Agencia_TipoDocumento_list")


class PromocionListView(generic.ListView):
    model = models.Promocion
    form_class = forms.PromocionForm


class PromocionCreateView(generic.CreateView):
    model = models.Promocion
    form_class = forms.PromocionForm


class PromocionDetailView(generic.DetailView):
    model = models.Promocion
    form_class = forms.PromocionForm
    pk_url_kwarg = "idPromocion"


class PromocionUpdateView(generic.UpdateView):
    model = models.Promocion
    form_class = forms.PromocionForm
    pk_url_kwarg = "idPromocion"


class PromocionDeleteView(generic.DeleteView):
    model = models.Promocion
    success_url = reverse_lazy("Agencia_Promocion_list")


class TipoPQRSListView(generic.ListView):
    model = models.TipoPQRS
    form_class = forms.TipoPQRSForm


class TipoPQRSCreateView(generic.CreateView):
    model = models.TipoPQRS
    form_class = forms.TipoPQRSForm


class TipoPQRSDetailView(generic.DetailView):
    model = models.TipoPQRS
    form_class = forms.TipoPQRSForm
    pk_url_kwarg = "idTipoPQRS"


class TipoPQRSUpdateView(generic.UpdateView):
    model = models.TipoPQRS
    form_class = forms.TipoPQRSForm
    pk_url_kwarg = "idTipoPQRS"


class TipoPQRSDeleteView(generic.DeleteView):
    model = models.TipoPQRS
    success_url = reverse_lazy("Agencia_TipoPQRS_list")


# class TransaccionListView(generic.ListView):
#     model = models.Transaccion
#     form_class = forms.TransaccionForm


# class TransaccionCreateView(generic.CreateView):
#     model = models.Transaccion
#     form_class = forms.TransaccionForm


# class TransaccionDetailView(generic.DetailView):
#     model = models.Transaccion
#     form_class = forms.TransaccionForm
#     pk_url_kwarg = "idTransaccion"
#
#
# class TransaccionUpdateView(generic.UpdateView):
#     model = models.Transaccion
#     form_class = forms.TransaccionForm
#     pk_url_kwarg = "idTransaccion"
#
#
# class TransaccionDeleteView(generic.DeleteView):
#     model = models.Transaccion
#     success_url = reverse_lazy("Agencia_Transaccion_list")


class CiudadListView(generic.ListView):
    model = models.Ciudad
    form_class = forms.CiudadForm


class CiudadCreateView(generic.CreateView):
    model = models.Ciudad
    form_class = forms.CiudadForm


class CiudadDetailView(generic.DetailView):
    model = models.Ciudad
    form_class = forms.CiudadForm
    pk_url_kwarg = "idCiudad"


class CiudadUpdateView(generic.UpdateView):
    model = models.Ciudad
    form_class = forms.CiudadForm
    pk_url_kwarg = "idCiudad"


class CiudadDeleteView(generic.DeleteView):
    model = models.Ciudad
    success_url = reverse_lazy("Agencia_Ciudad_list")


# class PQRSListView(generic.ListView):
#     model = models.PQRS
#     form_class = forms.PQRSForm


# class PQRSCreateView(generic.CreateView):
#     model = models.PQRS
#     form_class = forms.PQRSForm
#
#
# class PQRSDetailView(generic.DetailView):
#     model = models.PQRS
#     form_class = forms.PQRSForm
#
#
# class PQRSUpdateView(generic.UpdateView):
#     model = models.PQRS
#     form_class = forms.PQRSForm
#     pk_url_kwarg = "pk"
#
#
# class PQRSDeleteView(generic.DeleteView):
#     model = models.PQRS
#     success_url = reverse_lazy("Agencia_PQRS_list")


class TransaccionPromocionListView(generic.ListView):
    model = models.TransaccionPromocion
    form_class = forms.TransaccionPromocionForm


class TransaccionPromocionCreateView(generic.CreateView):
    model = models.TransaccionPromocion
    form_class = forms.TransaccionPromocionForm


class TransaccionPromocionDetailView(generic.DetailView):
    model = models.TransaccionPromocion
    form_class = forms.TransaccionPromocionForm
    pk_url_kwarg = "idTransaccionPromocion"


class TransaccionPromocionUpdateView(generic.UpdateView):
    model = models.TransaccionPromocion
    form_class = forms.TransaccionPromocionForm
    pk_url_kwarg = "idTransaccionPromocion"


class TransaccionPromocionDeleteView(generic.DeleteView):
    model = models.TransaccionPromocion
    success_url = reverse_lazy("Agencia_TransaccionPromocion_list")


class PaisListView(generic.ListView):
    model = models.Pais
    form_class = forms.PaisForm


class PaisCreateView(generic.CreateView):
    model = models.Pais
    form_class = forms.PaisForm


class PaisDetailView(generic.DetailView):
    model = models.Pais
    form_class = forms.PaisForm
    pk_url_kwarg = "idPais"


class PaisUpdateView(generic.UpdateView):
    model = models.Pais
    form_class = forms.PaisForm
    pk_url_kwarg = "idPais"


class PaisDeleteView(generic.DeleteView):
    model = models.Pais
    success_url = reverse_lazy("Agencia_Pais_list")


class CuponListView(generic.ListView):
    model = models.Cupon
    form_class = forms.CuponForm


class CuponCreateView(generic.CreateView):
    model = models.Cupon
    form_class = forms.CuponForm


class CuponDetailView(generic.DetailView):
    model = models.Cupon
    form_class = forms.CuponForm
    pk_url_kwarg = "idCupon"


class CuponUpdateView(generic.UpdateView):
    model = models.Cupon
    form_class = forms.CuponForm
    pk_url_kwarg = "idCupon"


class CuponDeleteView(generic.DeleteView):
    model = models.Cupon
    success_url = reverse_lazy("Agencia_Cupon_list")


class ImagenListView(generic.ListView):
    model = models.Imagen
    form_class = forms.ImagenForm


class ImagenCreateView(generic.CreateView):
    model = models.Imagen
    form_class = forms.ImagenForm


class ImagenDetailView(generic.DetailView):
    model = models.Imagen
    form_class = forms.ImagenForm
    pk_url_kwarg = "idImagen"


class ImagenUpdateView(generic.UpdateView):
    model = models.Imagen
    form_class = forms.ImagenForm
    pk_url_kwarg = "idImagen"


class ImagenDeleteView(generic.DeleteView):
    model = models.Imagen
    success_url = reverse_lazy("Agencia_Imagen_list")


class PromocionImagenListView(generic.ListView):
    model = models.PromocionImagen
    form_class = forms.PromocionImagenForm


class PromocionImagenCreateView(generic.CreateView):
    model = models.PromocionImagen
    form_class = forms.PromocionImagenForm


class PromocionImagenDetailView(generic.DetailView):
    model = models.PromocionImagen
    form_class = forms.PromocionImagenForm
    pk_url_kwarg = "idPromocionImagen"


class PromocionImagenUpdateView(generic.UpdateView):
    model = models.PromocionImagen
    form_class = forms.PromocionImagenForm
    pk_url_kwarg = "idPromocionImagen"


class PromocionImagenDeleteView(generic.DeleteView):
    model = models.PromocionImagen
    success_url = reverse_lazy("Agencia_PromocionImagen_list")


class PlanTuristicoListView(generic.ListView):
    model = models.PlanTuristico
    form_class = forms.PlanTuristicoForm


class PlanTuristicoCreateView(generic.CreateView):
    model = models.PlanTuristico
    form_class = forms.PlanTuristicoForm


class PlanTuristicoDetailView(generic.DetailView):
    model = models.PlanTuristico
    form_class = forms.PlanTuristicoForm
    pk_url_kwarg = "idPlan"


class PlanTuristicoUpdateView(generic.UpdateView):
    model = models.PlanTuristico
    form_class = forms.PlanTuristicoForm
    pk_url_kwarg = "idPlan"


class PlanTuristicoDeleteView(generic.DeleteView):
    model = models.PlanTuristico
    success_url = reverse_lazy("Agencia_PlanTuristico_list")


class ClienteListView(generic.ListView):
    model = models.Cliente
    form_class = forms.ClienteForm


class ClienteCreateView(generic.CreateView):
    model = models.Cliente
    form_class = forms.ClienteForm


class ClienteDetailView(generic.DetailView):
    model = models.Cliente
    form_class = forms.ClienteForm
    pk_url_kwarg = "idCliente"


class ClienteUpdateView(generic.UpdateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    pk_url_kwarg = "idCliente"


class ClienteDeleteView(generic.DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("Agencia_Cliente_list")
