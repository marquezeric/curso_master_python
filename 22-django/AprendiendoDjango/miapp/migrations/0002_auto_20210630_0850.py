# Generated by Django 3.1.5 on 2021-06-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='null', upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=110),
        ),
    ]
