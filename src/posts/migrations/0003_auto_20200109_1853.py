# Generated by Django 3.0.2 on 2020-01-09 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='timestamps',
            new_name='timestamp',
        ),
    ]
