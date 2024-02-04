# Generated by Django 5.0.1 on 2024-02-04 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_rename_books_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author_id',
        ),
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.RemoveField(
            model_name='member',
            name='id',
        ),
        migrations.AddField(
            model_name='author',
            name='timestampedmodel_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.timestampedmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='timestampedmodel_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.timestampedmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='timestampedmodel_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.timestampedmodel'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_app.timestampedmodel')),
                ('transaction_type', models.CharField(choices=[('CHECKOUT', 'checkout'), ('RESERVATION', 'reservation')], max_length=20)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.book')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.member')),
            ],
            bases=('my_app.timestampedmodel',),
        ),
    ]