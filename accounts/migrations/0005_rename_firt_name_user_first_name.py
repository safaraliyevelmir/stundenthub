# Generated by Django 4.2.1 on 2023-05-10 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firt_name',
            new_name='first_name',
        ),
    ]
