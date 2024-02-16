from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Supplier(models.Model):
    """Поставщик"""

    name = models.CharField(max_length=100, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='почта')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house_number = models.CharField(max_length=10, verbose_name='номер дома')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'


class Product(models.Model):
    """Продукт"""

    name = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность поставщика')
    debt = models.BooleanField(default=False, verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class NetworkElement(models.Model):
    """Элемент сети"""

    TYPE_CHOICES = (
        ('Factory', 'Завод'),
        ('RetailNetwork', 'Розничная сеть'),
        ('IndividualEntrepreneur', 'Индивидуальный предприниматель'),
    )
    name = models.CharField(max_length=100, verbose_name='название')
    contact_email = models.EmailField(verbose_name='почта')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house_number = models.CharField(max_length=10, verbose_name='номер дома')
    level = models.PositiveSmallIntegerField(verbose_name='уровень')
    element_type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name='тип элемента сети')
    products = models.ManyToManyField(Product, verbose_name='продукты')

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplied_to', **NULLABLE,
                                 verbose_name='поставщик')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'сеть'
        verbose_name_plural = 'сети'
