# Generated by Django 4.1.7 on 2023-05-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0011_articleimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleimage',
            name='image',
            field=models.ImageField(upload_to='photos', verbose_name='Фото'),
        ),
    ]
