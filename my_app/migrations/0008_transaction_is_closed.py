# Generated by Django 5.0.1 on 2024-02-04 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_alter_transaction_collection_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_closed',
            field=models.BooleanField(default=True),
        ),
    ]