# Generated by Django 4.1.7 on 2023-04-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('code', models.IntegerField()),
                ('expiration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
