from django.contrib import admin
from cars.models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)


class CarAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "model",
        "brand",
        # "factory_year",
        "model_year",
        # "description",
        "price",
        "photo",
    )
    search_fields = ("name", "model", "brand")
    list_filter = ("brand", "factory_year", "model_year")


# registers the models in the admin panel
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
