# Generated by Django 4.2.1 on 2023-05-10 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tag'),
        ('accounts', '0003_user_specialty_user_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(to='main.tag'),
        ),
    ]