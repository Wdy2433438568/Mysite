# Generated by Django 3.1.7 on 2021-03-12 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='cls',
        ),
        migrations.DeleteModel(
            name='cls',
        ),
        migrations.DeleteModel(
            name='student',
        ),
        migrations.DeleteModel(
            name='teacher',
        ),
    ]
