# Generated by Django 4.2.7 on 2024-01-17 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0029_contract_organizer_team_victor_player_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cranks',
            old_name='cranks_name',
            new_name='Cname',
        ),
    ]