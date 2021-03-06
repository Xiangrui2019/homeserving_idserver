# Generated by Django 3.1 on 2020-08-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id', '0002_auto_20200829_1030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userrole',
            options={'verbose_name': '用户角色'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(default='https://xiangrui.aiur.site/favicon.PNG', max_length=128, verbose_name='头像地址'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bili_bili',
            field=models.CharField(default='无', max_length=128, verbose_name='bilibili'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='qq',
            field=models.CharField(default='无', max_length=128, verbose_name='QQ'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='youtube',
            field=models.CharField(default='无', max_length=128, verbose_name='Youtube'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='github',
            field=models.CharField(default='无', max_length=128, verbose_name='Github'),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='user',
            field=models.ManyToManyField(to='id.UserProfile', verbose_name='属于这个角色的用户'),
        ),
    ]
