# Generated by Django 4.1.7 on 2023-03-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0006_articleimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleimage',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Фото'),
        ),
    ]