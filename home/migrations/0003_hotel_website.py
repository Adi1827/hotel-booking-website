# Generated by Django 4.2.4 on 2023-09-28 13:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220518_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='website',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
