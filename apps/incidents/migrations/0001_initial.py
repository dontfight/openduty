# Generated by Django 2.1.3 on 2018-11-22 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_key', models.CharField(max_length=200)),
                ('event_type', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('occurred_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'incidents',
                'verbose_name_plural': 'incidents',
            },
        ),
        migrations.CreateModel(
            name='IncidentSilenced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('silenced', models.BooleanField(default=False)),
                ('silenced_until', models.DateTimeField()),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incidents.Incident')),
            ],
        ),
    ]
