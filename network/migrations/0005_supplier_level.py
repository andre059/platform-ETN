# Generated by Django 5.0.2 on 2024-02-17 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_networkelement_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='level',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='уровень'),
        ),
    ]