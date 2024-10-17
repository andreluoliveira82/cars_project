from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm


def home_view(request):
    return render(request, "home.html")


def cars_view(request):
    """Quando o usuario 'bater' na rota cars, esta função será chamada e retornará a lista de carros.
    se o usuario passar um parametro na url, como search=Fiat, a função irá filtrar os carros com o nome Fiat.

    Args:
        request (_type_): _description_
    """
    cars = Car.objects.all().order_by("brand__name")

    search = request.GET.get("search")

    if search:
        # contains filtro que busca por palavras que contenham o valor passado
        # cars = cars.filter(model__contains=search)

        # icontains é o mesmo, mas não diferencia maiúsculas e minúsculas (o i é de ignore case)
        cars = cars.filter(model__icontains=search)
        
    return render(request, "cars.html", {"cars": cars})


def new_car_view(request):
    """_summary_: Quando o usuario 'bater' na rota new_car, esta função será chamada e
     o metodo GET será devolvido. Assim renderizamos na página o formulário para criar um novo carro.

     Quando o usuario clicar no botão submit, o metodo POST será chamado e o novo carro será criad no database.

    Args:
        request (http request): _é o objeto que contém todas as informações da requisição do usuário.

    Returns:
        response http: _o que será devolvido para o usuário.
    """
    if request.method == "POST":
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect("cars_list")
    else:
        new_car_form = CarModelForm()
    return render(request, "new_car.html", context={"new_car_form": new_car_form})
