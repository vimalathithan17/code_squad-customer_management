# Generated by Django 4.2.4 on 2023-08-29 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail_management', '0004_remove_travelhistory_date_travelhistory_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travelhistory',
            old_name='destinstion',
            new_name='destination',
        ),
    ]
