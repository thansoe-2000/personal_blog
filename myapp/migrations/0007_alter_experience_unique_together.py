# Generated by Django 4.2.2 on 2023-06-27 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_experience_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='experience',
            unique_together={('carrier', 'slug')},
        ),
    ]