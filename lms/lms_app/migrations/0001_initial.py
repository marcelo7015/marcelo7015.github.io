# Generated by Django 2.0.6 on 2018-09-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('celular', models.TextField(max_length=20)),
                ('login', models.TextField(max_length=20)),
                ('senha', models.TextField(max_length=20)),
            ],
        ),
    ]
