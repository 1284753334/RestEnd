# Generated by Django 3.0.7 on 2020-07-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20200718_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='u_username',
            new_name='u_name',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='u_password',
            field=models.CharField(max_length=256),
        ),
    ]
