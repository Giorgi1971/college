# Generated by Django 3.2 on 2021-09-30 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pupil',
            options={'verbose_name': 'Pupil', 'verbose_name_plural': 'Pupils'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
    ]