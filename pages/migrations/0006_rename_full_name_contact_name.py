# Generated by Django 3.2.9 on 2022-01-03 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='full_name',
            new_name='name',
        ),
    ]