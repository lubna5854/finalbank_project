# Generated by Django 4.2.1 on 2023-08-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
            ],
        ),
    ]
