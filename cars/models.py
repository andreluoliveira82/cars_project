from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, verbose_name="Nome")

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, verbose_name="Nome")
    model = models.CharField(max_length=40, verbose_name="Modelo")
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name="car_brand", verbose_name="Marca"
    )
    factor_year = models.IntegerField(
        verbose_name="Ano Fabricação", blank=True, null=True
    )
    model_year = models.IntegerField(verbose_name="Ano Modelo", blank=True, null=True)
    plate = models.CharField(max_length=7, verbose_name="Placa", blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Preço", blank=True, null=True
    )
    description = models.TextField(verbose_name="Descrição", blank=True, null=True)
    photo = models.ImageField(
        upload_to="cars/", verbose_name="Foto", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    # sobreescrevemos o método __str__ para evitar que o objeto fique como 'object' no site
    def __str__(self) -> str:
        return self.model # model aqui é o modelo do carro (nao a model do sistema)
