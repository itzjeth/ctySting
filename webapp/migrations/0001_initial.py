# Generated by Django 4.2.7 on 2023-12-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]