from django.shortcuts import render
from cars.models import Car


def home_view(request):
    return render(request, "home.html")


def cars_view(request):
    """Quando o usuario 'bater' na rota cars, esta função será chamada e retornará a lista de carros.
    se o usuario passar um parametro na url, como search=Fiat, a função irá filtrar os carros com o nome Fiat.

    Args:
        request (_type_): _description_
    """
    cars = Car.objects.all().order_by(
        "brand__name",
    )  # para ordenar decrescente: order_by("-brand__name", )
    
    search = request.GET.get("search")

    if search:
        # cars = cars.filter(model__contains=search) # contains filtro que busca por palavras que contenham o valor passado
        cars = cars.filter(
            model__icontains=search
        )  # icontains é o mesmo, mas não diferencia maiúsculas e minúsculas (o i é de ignore case)
    return render(request, "cars.html", {"cars": cars})
