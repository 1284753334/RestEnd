# Generated by Django 3.0.7 on 2020-07-18 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200718_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='a_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.UserModel'),
        ),
    ]