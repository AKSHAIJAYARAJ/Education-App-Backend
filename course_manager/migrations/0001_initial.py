# Generated by Django 4.2.3 on 2023-07-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('course_name', models.CharField(blank=True, max_length=200, null=True)),
                ('course_description', models.CharField(blank=True, max_length=200, null=True)),
                ('course_rating', models.FloatField(blank=True, null=True)),
                ('course_price', models.FloatField(blank=True, null=True)),
                ('course_discount', models.FloatField(blank=True, null=True)),
                ('course_status', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
