# Generated by Django 2.1.7 on 2019-02-26 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='bank',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
    ]
