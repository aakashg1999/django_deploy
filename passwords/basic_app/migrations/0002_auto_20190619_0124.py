# Generated by Django 2.2.1 on 2019-06-18 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_pic',
            new_name='profile_pic',
        ),
    ]
