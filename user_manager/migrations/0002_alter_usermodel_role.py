# Generated by Django 4.2.3 on 2023-07-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='role',
            field=models.CharField(blank=True, default='student', max_length=13, null=True),
        ),
    ]
