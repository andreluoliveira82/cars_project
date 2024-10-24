from typing import Any
from django import forms

from cars.models import Brand, Car


# ============================================
# criando um form na unha usando o Form do Django
# class CarForm(forms.Form):
#     brand = forms.ModelChoiceField(queryset=Brand.objects.all().order_by("name"))
#     name = forms.CharField(max_length=40)
#     model = forms.CharField(max_length=40)
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     price = forms.FloatField()
#     description = forms.CharField(widget=forms.Textarea)
#     photo = forms.ImageField()

#     def save(self):
#         """Salva efetivamente os dados no database"""
#         car = Car(
#             brand=self.cleaned_data["brand"],
#             name=self.cleaned_data["name"],
#             model=self.cleaned_data["model"],
#             factory_year=self.cleaned_data["factory_year"],
#             model_year=self.cleaned_data["model_year"],
#             plate=self.cleaned_data["plate"],
#             price=self.cleaned_data["price"],
#             description=self.cleaned_data["description"],
#             photo=self.cleaned_data["photo"],
#         )
#         car.save()
#         return car


# ================================================
# Criando o mesmo form acima utilizando o Model Form do Django
class CarModelForm(forms.ModelForm):
    """Gera um formulário com base na model desejada

    Args:
        forms (Django ModelForm): ModelForm do Django
    """

    class Meta:
        model = Car
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordena o campo 'brand' em ordem alfabética
        self.fields["brand"].queryset = Brand.objects.order_by("name")

    # methods to validate fields in form
    #
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 3:
            raise forms.ValidationError(
                "O nome do carro deve ter pelo menos 3 caracteres"
            )
        return name

    def clean_model_year(self):
        """Validar se o ano de modelo do carro é válido
        o ano de modelo do carro deve ser igual ao ano de fabricação ou +1
        Exemplo: factory_year: 1988
                model_year: 1988 ou no maximo 1999.
        """
        model_year = self.cleaned_data.get("model_year")
        factory_year = self.cleaned_data.get("factory_year")

        if model_year < factory_year or model_year > factory_year + 1:
            self.add_error(
                "model_year",
                "O ano modelo deve ser igual ao ano de fabriação ou o ano de fabricação + 1 ",
            )
        return model_year


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if name == "" or len(name) < 3:
            self.add_error(
                field="name",
                error="Informe a marca. O nome da marca deve ter ao menos 03 caracteres.",
            )
        return name
