# Generated by Django 4.2.5 on 2023-10-18 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_register_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('number', models.IntegerField(default=0)),
                ('comments', models.CharField(max_length=70)),
            ],
        ),
    ]
