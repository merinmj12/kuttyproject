# Generated by Django 2.2 on 2021-11-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuttyapp', '0002_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
