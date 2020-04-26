# Generated by Django 3.0.5 on 2020-04-24 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200424_0418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='post',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog_images/'),
        ),
    ]
