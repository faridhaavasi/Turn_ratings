# Generated by Django 4.1.7 on 2023-04-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_file_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='token',
            field=models.CharField(blank=True, max_length=50, null=type, unique=True),
            preserve_default=type,
        ),
    ]
