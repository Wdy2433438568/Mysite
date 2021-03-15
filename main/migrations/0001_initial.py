# Generated by Django 3.1.7 on 2021-03-12 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('in_date', models.DateField(auto_now_add=True)),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女')])),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.cls')),
            ],
        ),
        migrations.AddField(
            model_name='cls',
            name='t',
            field=models.ManyToManyField(to='main.teacher'),
        ),
    ]
