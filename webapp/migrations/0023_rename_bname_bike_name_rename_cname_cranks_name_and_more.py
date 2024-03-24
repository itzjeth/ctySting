# Generated by Django 4.2.7 on 2024-01-15 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_rename_bname_bike_bname_rename_cname_cranks_cname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='bname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='cranks',
            old_name='cname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='frames',
            old_name='fname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='handlebars',
            old_name='hname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='wheels',
            old_name='wname',
            new_name='name',
        ),
    ]