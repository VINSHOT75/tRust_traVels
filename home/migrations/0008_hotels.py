# Generated by Django 3.1.7 on 2021-04-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_image_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('desc', models.CharField(default='', max_length=100000)),
                ('hotel_img', models.ImageField(upload_to='img/%y')),
                ('price', models.IntegerField(default='0')),
            ],
        ),
    ]
