# Generated by Django 5.0.1 on 2024-01-11 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='name',
            field=models.CharField(default='Default', max_length=255),
            preserve_default=False,
        ),
    ]