# Generated by Django 4.0.6 on 2022-07-23 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastlane', '0008_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('profile', models.ImageField(upload_to='team_profile/%y')),
            ],
        ),
    ]
