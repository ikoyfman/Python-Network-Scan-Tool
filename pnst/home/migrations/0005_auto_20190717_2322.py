# Generated by Django 2.2.3 on 2019-07-17 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_scan_task_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scan',
            old_name='stauts',
            new_name='status',
        ),
    ]
