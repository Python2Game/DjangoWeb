# Generated by Django 3.1.3 on 2020-11-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Ваше имя')),
                ('title', models.CharField(max_length=40, verbose_name='Название услуги')),
            ],
        ),
    ]
