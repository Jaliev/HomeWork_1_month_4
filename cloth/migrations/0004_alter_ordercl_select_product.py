# Generated by Django 4.2.6 on 2023-11-09 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0003_remove_ordercl_name_ordercl_client_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercl',
            name='select_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orger_product', to='cloth.productcl', verbose_name='Выберите товар'),
        ),
    ]
