# Generated by Django 2.2.3 on 2019-07-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
