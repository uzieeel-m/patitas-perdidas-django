# Generated by Django 4.1.3 on 2022-12-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mascotas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mascota",
            name="imagen",
            field=models.ImageField(blank=True, null=True, upload_to="media/img/"),
        ),
    ]