# Generated by Django 3.0 on 2021-02-11 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='Contact',
        ),
    ]