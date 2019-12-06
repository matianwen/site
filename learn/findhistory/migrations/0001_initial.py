# Generated by Django 2.1.10 on 2019-12-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Findnearhistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, verbose_name='作者')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], default='男', max_length=32, verbose_name='性别')),
                ('placename', models.CharField(max_length=20, verbose_name='地名')),
                ('history', models.TextField(null=True, verbose_name='内容')),
                ('timenow', models.DateTimeField(auto_now_add=True)),
                ('see', models.IntegerField(default=0, verbose_name='浏览数')),
            ],
            options={
                'verbose_name': '挖掘历史',
                'verbose_name_plural': '挖掘历史',
            },
        ),
    ]
