# Generated by Django 2.2.11 on 2020-08-06 20:58

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_listemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='json',
            field=jsonfield.fields.JSONField(default={'pages_progress': {}}),
        ),
    ]