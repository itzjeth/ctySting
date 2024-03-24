# Generated by Django 4.2.7 on 2024-01-15 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_rename_bike_name_bike_bike_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='bike_name',
            new_name='Bname',
        ),
        migrations.RenameField(
            model_name='cranks',
            old_name='crank_name',
            new_name='Cname',
        ),
        migrations.RenameField(
            model_name='frames',
            old_name='frame_name',
            new_name='Fname',
        ),
        migrations.RenameField(
            model_name='handlebars',
            old_name='handlebar_name',
            new_name='Hname',
        ),
        migrations.RenameField(
            model_name='wheels',
            old_name='wheel_name',
            new_name='Wname',
        ),
    ]