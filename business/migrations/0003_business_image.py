# Generated by Django 3.2.14 on 2022-09-17 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_alter_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='image',
            field=models.ImageField(null=True, upload_to='business'),
        ),
    ]
