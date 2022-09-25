# Generated by Django 4.1.1 on 2022-09-25 08:22

import accounts.utils
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.CharField(default=accounts.utils.generate_user_id, max_length=10, unique=True, verbose_name='User ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('avatar', models.FileField(blank=True, null=True, upload_to='avatars/')),
                ('role', models.CharField(choices=[('SU', 'Super User'), ('CU', 'Customer'), ('OR', 'Owner'), ('OA', 'Organization Admin')], default='CU', max_length=2, verbose_name='User Role')),
                ('is_email_verified', models.BooleanField(default=False, help_text="Check to verify user's email.")),
                ('is_phone_verified', models.BooleanField(default=False, help_text="Check to verify user's phone number.")),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('last_login_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='organization.organization')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
                'unique_together': {('organization', 'email')},
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
    ]
