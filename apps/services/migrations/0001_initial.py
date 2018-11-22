# Generated by Django 2.1.3 on 2018-11-22 11:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedules', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('name', models.CharField(max_length=80, unique=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('retry', models.IntegerField(blank=True, null=True)),
                ('escalate_after', models.IntegerField(blank=True, null=True)),
                ('notifications_disabled', models.BooleanField(default=False)),
                ('send_resolve_enabled', models.BooleanField(default=False)),
                ('policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedules.SchedulePolicy')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'service',
            },
        ),
        migrations.CreateModel(
            name='ServiceSilenced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('silenced', models.BooleanField(default=False)),
                ('silenced_until', models.DateTimeField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTokens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
                ('token_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Token')),
            ],
            options={
                'verbose_name': 'service_tokens',
                'verbose_name_plural': 'service_tokens',
            },
        ),
    ]
