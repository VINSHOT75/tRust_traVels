# Generated by Django 3.1.7 on 2021-04-28 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_merge_20210428_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]