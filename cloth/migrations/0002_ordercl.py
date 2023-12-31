# Generated by Django 4.2.6 on 2023-11-08 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(max_length=5, verbose_name='Укажите количество')),
                ('name', models.CharField(max_length=100, verbose_name='Введите имя')),
                ('phone_number', models.CharField(default='+996', max_length=13, verbose_name='Введите номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Введите ваш email')),
                ('adress', models.CharField(max_length=100, verbose_name='Укажите адрес доставки')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('select_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orger_product', to='cloth.productcl')),
            ],
        ),
    ]
