# Generated by Django 4.1.6 on 2023-02-06 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pench', '0007_alter_file_file_alter_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='description',
        ),
    ]