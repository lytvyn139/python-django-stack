# Generated by Django 3.0.7 on 2020-06-14 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onetomanyApp', '0002_author_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='gender',
        ),
    ]