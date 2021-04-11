# Generated by Django 2.1.5 on 2021-04-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_homepage_link_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2083)),
                ('image_url', models.CharField(max_length=2083)),
                ('news_link', models.CharField(max_length=255)),
            ],
        ),
    ]
