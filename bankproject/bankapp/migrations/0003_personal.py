# Generated by Django 4.2.1 on 2023-08-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_user_delete_pics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=250)),
                ('Lastname', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=250)),
                ('Phone_number', models.CharField(max_length=250)),
                ('Gender', models.CharField(max_length=250)),
                ('Address', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('account_type', models.CharField(max_length=250)),
                ('material_debit_card', models.BooleanField(default=False)),
                ('material_credit_card', models.BooleanField(default=False)),
                ('material_atm_card', models.BooleanField(default=False)),
            ],
        ),
    ]
