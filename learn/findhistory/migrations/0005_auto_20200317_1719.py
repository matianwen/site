# Generated by Django 2.1.10 on 2020-03-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findhistory', '0004_auto_20200106_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findnearhistory',
            name='photo',
            field=models.FileField(default='headimages/history.jpg', upload_to='headimages/%Y/%m/%d/', verbose_name='图片'),
        ),
    ]
