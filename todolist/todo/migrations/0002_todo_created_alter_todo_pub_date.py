# Generated by Django 4.0.2 on 2022-03-05 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created',
            field=models.DateField(default='2022-03-05'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='pub_date',
            field=models.DateTimeField(default='2022-03-05'),
        ),
    ]
