# Generated by Django 4.1.1 on 2022-09-08 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('pet_ID', models.AutoField(primary_key=True, serialize=False)),
                ('pet_name', models.CharField(max_length=120)),
                ('pet_owner_name', models.CharField(max_length=120)),
                ('pet_age', models.IntegerField()),
                ('pet_type', models.CharField(max_length=120)),
                ('pet_gender', models.CharField(max_length=10)),
            ],
        ),
    ]
