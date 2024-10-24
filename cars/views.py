from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from cars.models import Brand, Car
from cars.forms import CarModelForm, BrandModelForm

# =======================CAR=============================


class HomeView(View):
    def get(self, request):
        return render(request, "home.html")


class CarsListView(ListView):
    """
    Exibe a lista de carros na pagina (view).
    Caso o usuario fizer um filtro (search), o metodo 'get_query' será executado.
    """

    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset().order_by("price")  # model = modelo carro

        search = self.request.GET.get("search")

        if search:
            # contains filtro que busca por palavras que contenham o valor passado
            # cars = cars.filter(model__contains=search)

            # icontains é o mesmo, mas não diferencia maiúsculas e minúsculas (o i é de ignore case)
            cars = cars.filter(model__icontains=search)
        return cars


class CarDetailView(DetailView):
    """
    Visualizar detalhes de um item específico

    """

    model = Car
    template_name = "car_detail.html"


@method_decorator(login_required(login_url="login"), name="dispatch")
class NewCarCreateView(CreateView):
    """Insert a new car in the database"""

    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = "/cars/"


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarUpdateView(UpdateView):
    """
    Atualizar um carro selecionado
    """

    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"

    # sobreescrevendo o metodo get_success_url para conseguir redirecionar para a página de detalhe do item
    def get_success_url(self) -> str:
        return reverse_lazy("car_detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarDeleteView(DeleteView):
    """
    Deletar um carro selecionado
    """

    model = Car
    template_name = "car_delete.html"
    success_url = "/cars/"


# =======================BRAND=============================


@method_decorator(login_required(login_url="login"), name="dispatch")
class NewBrandCreateView(CreateView):
    """Create a new brand"""

    model = Brand
    form_class = BrandModelForm
    template_name = "new_brand.html"
    success_url = "/new_brand/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona a lista de marcas ao contexto
        context["brands"] = Brand.objects.order_by("name")
        return context
