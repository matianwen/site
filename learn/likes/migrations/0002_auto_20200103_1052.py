# Generated by Django 2.1.10 on 2020-01-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likecount',
            options={'verbose_name': '点赞统计', 'verbose_name_plural': '点赞统计'},
        ),
        migrations.AlterModelOptions(
            name='likerecord',
            options={'verbose_name': '点赞记录', 'verbose_name_plural': '点赞记录'},
        ),
        migrations.AlterField(
            model_name='likerecord',
            name='user',
            field=models.CharField(max_length=16),
        ),
    ]
