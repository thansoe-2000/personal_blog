# Generated by Django 4.2.2 on 2023-06-26 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_contact_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='full_name',
            new_name='fullname',
        ),
    ]
