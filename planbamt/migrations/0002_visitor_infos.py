# Generated by Django 4.0.4 on 2022-05-28 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planbamt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor_Infos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('page_visited', models.TextField()),
                ('event_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
