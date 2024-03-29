# Generated by Django 5.0.2 on 2024-02-15 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('debt_to_supplier', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=10)),
                ('level', models.PositiveSmallIntegerField()),
                ('element_type', models.CharField(choices=[('Factory', 'Завод'), ('RetailNetwork', 'Розничная сеть'), ('IndividualEntrepreneur', 'Индивидуальный предприниматель')], max_length=35)),
                ('products', models.ManyToManyField(to='network.product')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplied_to', to='network.supplier')),
            ],
        ),
    ]
