# Generated by Django 4.1.7 on 2023-05-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_alter_user_options_remove_user_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='user',
            name='file_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='شماره پرونده'),
        ),
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نام بیمار'),
        ),
    ]