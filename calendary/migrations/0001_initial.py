# Generated by Django 3.2.4 on 2021-09-30 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(default=' SOME STRING', max_length=15)),
                ('event_task', models.TextField(max_length=80, null=True)),
                ('event_duration', models.TimeField(null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
