# Generated by Django 3.1.1 on 2020-09-13 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image_url',
        ),
    ]
