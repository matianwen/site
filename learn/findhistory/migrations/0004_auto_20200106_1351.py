# Generated by Django 2.1.10 on 2020-01-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findhistory', '0003_auto_20191207_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findnearhistory',
            name='username',
            field=models.CharField(default='admin', max_length=16, verbose_name='作者'),
        ),
    ]
