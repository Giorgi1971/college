# Generated by Django 3.2 on 2021-10-09 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210930_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user/teachers'),
        ),
    ]
