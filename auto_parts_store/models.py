from django.db import models

class AutoParts(models.Model):
    BRAND = (
        ('Mitsubishi', 'Mitsubishi'),
        ('Jeep', 'Jeep'),
        ('Land Rover', 'Land Rover'),
        ('Isuzu', 'Isuzu'),
        ('Nissan', 'Nissan'),
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford')
    )
    YEAR = (
        ('1980-1984', '1980-1984'),
        ('1985-1989', '1985-1989'),
        ('1990-1994', '1990-1994'),
        ('1995-1999', '1995-1999'),
        ('2000-2004', '2000-2004'),
        ('2005-2009', '2005-2009'),
        ('2010-2014', '2010-2014'),
        ('2015-2019', '2015-2019'),
        ('2020-2023', '2020-2023')
    )
    title = models.CharField('Укажите название товара', max_length=100)
    image = models.ImageField('Загрузите фото', upload_to='products/')
    description = models.TextField('Укажите описание товара')
    car_brand = models.CharField('Выберите марку автомобиля', max_length=100, choices=BRAND)
    year_of_release = models.CharField('Выберите год выпуска', max_length=100, choices=YEAR)
    review_of_the_car = models.URLField('Укажите видео обзор автомобиля', blank=True)
    review_of_auto_parts = models.URLField('Укажите видео обзор автозапчасти', blank=True)
    cost = models.TextField('Укажите цену')
    tel_number = models.IntegerField('Укажите номер телефона', null=True)
    Email = models.EmailField('Укажите вашу почту', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}.{self.car_brand}'
