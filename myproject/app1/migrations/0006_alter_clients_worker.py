# Generated by Django 4.2.2 on 2023-06-18 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_company_products_clients_compani_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='worker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='related_name', to='app1.worker'),
        ),
    ]