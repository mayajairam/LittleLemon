# Generated by Django 5.1.5 on 2025-03-13 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0008_employees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employees',
            old_name='count',
            new_name='shift',
        ),
    ]
