# Generated by Django 4.1.1 on 2022-09-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be', '0003_alter_pets_pet_age_alter_pets_pet_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='pet_gender',
            field=models.CharField(choices=[('NB', 'Non-Binary'), ('M', 'Male'), ('F', 'Female')], default='NB', max_length=2),
        ),
    ]
