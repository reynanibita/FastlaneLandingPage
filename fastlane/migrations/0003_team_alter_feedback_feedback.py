# Generated by Django 4.0.6 on 2022-07-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastlane', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(),
        ),
    ]
