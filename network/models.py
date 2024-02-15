from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class NetworkElement(models.Model):
    TYPE_CHOICES = (
        ('Factory', 'Завод'),
        ('RetailNetwork', 'Розничная сеть'),
        ('IndividualEntrepreneur', 'Индивидуальный предприниматель'),
    )
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    level = models.PositiveSmallIntegerField()
    element_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    products = models.ManyToManyField(Product)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplied_to', null=True, blank=True)

    def __str__(self):
        return self.name
