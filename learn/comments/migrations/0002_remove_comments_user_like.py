# Generated by Django 2.1.10 on 2019-12-11 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user_like',
        ),
    ]
