# Generated by Django 5.0 on 2023-12-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=15)),
                ('date', models.DateField()),
                ('artist', models.TextField()),
            ],
        ),
    ]
