# Generated by Django 5.2.1 on 2025-07-07 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0004_alter_potholereport_priority"),
    ]

    operations = [
        migrations.RenameField(
            model_name="potholereport",
            old_name="priority",
            new_name="severity",
        ),
    ]
