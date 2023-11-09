from django.db import models

class CustomerCL(models.Model):
    name = models.CharField(max_length=100, verbose_name='Введите имя')
    phone = models.CharField(max_length=13, default='+996', verbose_name='Введите номер телефона')
    email = models.EmailField(verbose_name='Введите email', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'

class TagCL(models.Model):
    name = models.CharField(max_length=100, verbose_name='Напишите тег')

    def __str__(self):
        return f'#{self.name}'

class ProductCL(models.Model):
    name = models.CharField(max_length=100, verbose_name='Введите название товара')
    image = models.ImageField(upload_to='product/')
    tags = models.ManyToManyField(TagCL, related_name='product_tags')

    def __str__(self):
        return self.name

class OrderCL(models.Model):
    select_product = models.ForeignKey(ProductCL, on_delete=models.CASCADE, related_name='orger_product', verbose_name='Выберите товар', null=True)
    quantity = models.IntegerField(max_length=5, verbose_name='Укажите количество')
    client_name = models.CharField(max_length=100, verbose_name='Введите имя', null=True)
    phone_number = models.CharField(max_length=13, default='+996', verbose_name='Введите номер телефона')
    email = models.EmailField(verbose_name='Введите ваш email', blank=True)
    adress = models.CharField(max_length=100, verbose_name='Укажите адрес доставки')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.select_product} - {self.adress}'

