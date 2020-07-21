# Generated by Django 3.0.7 on 2020-07-18 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_username', models.CharField(max_length=32, unique=True)),
                ('u_password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_address', models.CharField(max_length=256)),
                ('a_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.UserModel')),
            ],
        ),
    ]
