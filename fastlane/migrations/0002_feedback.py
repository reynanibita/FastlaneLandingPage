# Generated by Django 4.0.6 on 2022-07-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastlane', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=150)),
                ('feedback', models.CharField(max_length=350)),
            ],
        ),
    ]
