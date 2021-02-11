# Generated by Django 3.0 on 2021-02-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]