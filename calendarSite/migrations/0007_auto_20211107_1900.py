# Generated by Django 2.1.7 on 2021-11-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarSite', '0006_auto_20211107_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='作成日'),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='更新日'),
        ),
    ]
