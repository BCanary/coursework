# Generated by Django 3.1.1 on 2020-09-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0005_book_image_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='', max_length=25),
        ),
    ]