# Generated by Django 4.2.6 on 2023-10-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0002_sponsor_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='is_legal',
            field=models.BooleanField(default=False),
        ),
    ]
