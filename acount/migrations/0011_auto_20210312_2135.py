# Generated by Django 3.1.7 on 2021-03-12 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0010_auto_20210312_2135'),
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
