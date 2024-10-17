# Generated by Django 5.1.2 on 2024-10-15 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40, verbose_name='Nome')),
                ('model', models.CharField(max_length=100, verbose_name='Modelo')),
                ('brand', models.CharField(max_length=40, verbose_name='Marca')),
                ('factor_year', models.IntegerField(blank=True, null=True, verbose_name='Ano Fabricação')),
                ('model_year', models.IntegerField(blank=True, null=True, verbose_name='Ano Modelo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço')),
            ],
        ),
    ]