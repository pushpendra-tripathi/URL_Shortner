# Generated by Django 3.2.5 on 2021-07-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('original_url', models.CharField(max_length=500)),
                ('expired', models.BooleanField(default=False)),
            ],
        ),
    ]
