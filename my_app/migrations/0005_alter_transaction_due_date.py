# Generated by Django 5.0.1 on 2024-02-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_member_total_fine_transaction_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='due_date',
            field=models.DateField(),
        ),
    ]
