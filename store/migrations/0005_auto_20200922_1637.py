# Generated by Django 3.1.1 on 2020-09-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20200922_0326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='attribute',
            field=models.CharField(max_length=200),
        ),
    ]