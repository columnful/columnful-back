# Generated by Django 3.2.9 on 2021-11-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20211122_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]