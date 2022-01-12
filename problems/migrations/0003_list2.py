# Generated by Django 4.0.1 on 2022-01-05 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='List2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=1000)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('explanation', models.CharField(max_length=3000)),
            ],
        ),
    ]
