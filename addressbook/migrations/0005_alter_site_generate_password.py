# Generated by Django 4.2.8 on 2024-02-20 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("addressbook", "0004_site_generate_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="generate_password",
            field=models.BooleanField(default=True),
        ),
    ]
