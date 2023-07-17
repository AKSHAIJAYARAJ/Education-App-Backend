# Generated by Django 4.2.3 on 2023-07-15 10:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('user_phone_number', models.CharField(blank=True, max_length=13, null=True)),
                ('user_email', models.CharField(blank=True, max_length=150, null=True)),
                ('user_password', models.CharField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('role', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
    ]
