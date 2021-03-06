# Generated by Django 2.2.13 on 2021-02-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0005_auto_20210201_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, verbose_name='Telegram Bot Token')),
            ],
            options={
                'verbose_name': 'Telegram Bot 设置',
                'verbose_name_plural': 'Telegram Bot 设置',
            },
        ),
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=models.CharField(max_length=512, verbose_name='邮箱地址 / Server 酱 SCKEY /             Pushover User Key / Bark key / 自定义网址 / Slack channel / Telegram chat_id'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.IntegerField(choices=[(0, '邮箱'), (1, '微信'), (2, 'pushover'), (3, 'Bark'), (4, '自定义通知'), (5, 'Slack'), (6, 'Telegram')], default='邮箱', verbose_name='通知方式类型'),
        ),
    ]
