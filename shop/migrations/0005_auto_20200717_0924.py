# Generated by Django 3.0.7 on 2020-07-17 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='lname',
        ),
    ]
