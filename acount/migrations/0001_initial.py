# Generated by Django 3.1.7 on 2021-03-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=64)),
                ('pwd', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
            ],
        ),
    ]
