# Generated by Django 3.0.6 on 2020-05-06 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frontpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Console',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='frontpage.Product')),
            ],
            bases=('frontpage.product',),
        ),
    ]
