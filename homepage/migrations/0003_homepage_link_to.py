# Generated by Django 2.1.5 on 2021-04-04 02:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='link_to',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
