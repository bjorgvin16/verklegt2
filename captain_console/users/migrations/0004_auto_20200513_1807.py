# Generated by Django 3.0.6 on 2020-05-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200513_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productview',
            name='dateOfView',
            field=models.DateTimeField(),
        ),
    ]
