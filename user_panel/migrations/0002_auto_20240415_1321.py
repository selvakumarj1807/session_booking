# Generated by Django 3.0.5 on 2024-04-15 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_auto_20240414_1420'),
        ('user_panel', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Session_booking',
            new_name='Session_booking2',
        ),
    ]