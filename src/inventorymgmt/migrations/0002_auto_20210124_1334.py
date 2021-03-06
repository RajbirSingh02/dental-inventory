# Generated by Django 3.1.4 on 2021-01-24 06:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventorymgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, choices=[('Furniture', 'Furniture'), ('Dental Equipment', 'Dental Equipment'), ('Phone', 'Phone')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(default='0', null=True),
        ),
    ]
