# Generated by Django 3.2.14 on 2022-09-11 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translations',
            old_name='resume',
            new_name='article',
        ),
    ]
