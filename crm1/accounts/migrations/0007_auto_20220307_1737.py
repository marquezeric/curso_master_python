# Generated by Django 3.2.8 on 2022-03-07 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220216_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
