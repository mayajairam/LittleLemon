# Generated by Django 5.1.5 on 2025-02-25 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_menucategory_remove_menu_cuisine_remove_menu_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='category_name', to='demoapp.menucategory'),
        ),
    ]
