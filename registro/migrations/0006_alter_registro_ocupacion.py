# Generated by Django 5.2 on 2025-04-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_alter_registro_ocupacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='ocupacion',
            field=models.CharField(choices=[('Desocupado', 'Desocupado'), ('Ama de Casa', 'Ama de Casa'), ('Trabajador Estatal', 'Trabajador Estatal'), ('Trabajador por Cuenta Propia', 'Trabajador por Cuenta Propia')], default='Desocupado', max_length=100),
        ),
    ]
