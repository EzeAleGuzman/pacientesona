# Generated by Django 4.2.3 on 2023-09-03 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Internos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interno',
            old_name='telefono',
            new_name='interno',
        ),
    ]
