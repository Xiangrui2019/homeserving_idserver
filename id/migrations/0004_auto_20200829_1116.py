# Generated by Django 3.1 on 2020-08-29 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id', '0003_auto_20200829_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='user',
            field=models.ManyToManyField(blank=True, to='id.UserProfile', verbose_name='属于这个角色的用户'),
        ),
    ]
