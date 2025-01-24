from django.db import models

from users.models import NULLABLE


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f'{self.name} ({self.model})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Supplier(models.Model):
    LEVELS = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255, verbose_name='название')
    level = models.IntegerField(choices=LEVELS, verbose_name='уровень', editable=False, **NULLABLE)
    email = models.EmailField(verbose_name='почта')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    house = models.CharField(max_length=10, verbose_name='дом')
    products = models.ManyToManyField(Product, verbose_name='продукты', **NULLABLE)
    supplier_of = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name='поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,
                                           verbose_name='задолженность поставщику')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.name


    def get_level(self):
        supplier = self.supplier_of
        if not supplier.supplier_of.exists():
            return dict(self.LEVELS).get(0, 'Неизвестно')
        elif supplier.supplier_of == 0:
            return dict(self.LEVELS).get(1, 'Неизвестно')
        elif supplier.supplier_of == 1 or supplier.supplier_of == 2:
            return dict(self.LEVELS).get(2, 'Неизвестно')

    def save(self, *args, **kwargs):
        supplier = self.supplier_of
        if supplier is None:
            self.level = 0
        elif supplier.level == 0:
            self.level = 1
        elif supplier.level == 1 or supplier.level == 2:
            self.level = 2
        super(Supplier, self).save(*args, **kwargs)


    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'