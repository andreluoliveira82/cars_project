from django.db.models import Sum
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory


def car_inventory_update() -> None:
    """calculando a quantidade de carros e o valor total"""
    cars_count = Car.objects.all().count()

    cars_value = Car.objects.aggregate(total_value=Sum("price"))["total_value"]

    # criando um registro no inventario ( atualizando o kardex)
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.description:
        instance.description = "Bio Gerada automaticamente"

    if not instance.photo:
        instance.photo = "no-photo.jpg"


# @receiver(pre_delete, sender=Car)
# def car_pre_delete(sender, instance, **kwargs): ...


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    """Atualiza o estoque (kardex) quando entrar um novo item"""
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    """Atualiza o estoque quando sair (baixar/deletar) um item"""
    car_inventory_update()
